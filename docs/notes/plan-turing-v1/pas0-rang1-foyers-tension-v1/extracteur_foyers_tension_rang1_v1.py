"""Extracteur déterministe sur processeur des foyers de tension et d'épicycles (Rang 1, v1).

Exécute strictement et sans aucune retouche a posteriori le protocole préenregistré et scellé dans
`prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1.md`
(empreinte SHA-256 : `dcc8de2e34cf871eb380e385789b25e97e779182fbe681bb6739f102de6e2e67`).

Règles respectées :
- Dépense : 0,00 dollar américain (extraction par `/usr/bin/pdftotext`, aucun appel externe).
- Lecture seule intégrale sur `/home/antigravity/lciric/controle-ia-travail`.
- Gardes d'arrêt explicites (`ErreurGardeRang1`) sans aucun repli silencieux (règle R5).
- Graines dérivées de `numpy.random.SeedSequence(2026112401)` par `spawn(5)` (règle R9).
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import datetime as dt
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

import numpy as np
from scipy import stats

# Permet d'importer controle_ia.prereg et controle_ia.scellement sans modifier le dépôt
DEPOT_RACINE = Path("/home/antigravity/lciric/controle-ia-travail")
if str(DEPOT_RACINE / "src") not in sys.path:
    sys.path.insert(0, str(DEPOT_RACINE / "src"))

from controle_ia.gardes import GardeArret  # noqa: E402
from controle_ia.prereg import exiger_prereg_scelle  # noqa: E402

EMPREINTE_PREREG_ATTENDUE = "dcc8de2e34cf871eb380e385789b25e97e779182fbe681bb6739f102de6e2e67"
GRAINE_MAITRESSE = 2026112401


class ErreurGardeRang1(RuntimeError):
    """Exception levée immédiatement lorsqu'une garde d'arrêt du préenregistrement est franchie."""


# ============================================================================
# Vocabulaires figés par le préenregistrement (sections 3, 4, 5 et 6)
# ============================================================================

ANCRAGE_MODELES: list[str] = [
    "language model", "language models", "llm", "llms",
    "neural network", "neural networks", "transformer", "transformers",
    "deep learning", "foundation model", "foundation models",
    "ai system", "ai systems", "ai agent", "ai agents",
    "machine learning", "reinforcement learning",
    "reasoning model", "reasoning models",
    "generative model", "generative models",
    "large model", "large models",
]

ANCRAGE_CONTROLE: list[str] = [
    "alignment", "misalignment", "aligned", "misaligned",
    "ai safety", "ai control", "control protocol",
    "trusted monitor", "untrusted model",
    "interpretability", "mechanistic",
    "linear probe", "linear probes", "probing",
    "sparse autoencoder", "sparse autoencoders", "sae", "saes",
    "activation steering", "representation engineering",
    "circuit", "circuits", "superposition",
    "polysemantic", "polysemanticity", "monosemantic", "monosemanticity",
    "deception", "deceptive", "scheming", "sandbagging", "sycophancy",
    "jailbreak", "jailbreaks", "jailbreaking",
    "backdoor", "backdoors", "trojan", "trojans",
    "sleeper agent", "sleeper agents", "red-teaming",
    "guardrail", "guardrails", "scalable oversight",
    "monitoring", "monitor", "monitors",
    "audit", "audits", "auditing",
    "reward hacking", "overoptimization", "goodhart",
    "unlearning", "refusal",
    "lie detector", "lie detection", "truthfulness", "honesty",
    "hallucination", "hallucinations", "adversarial",
    "watermark", "watermarking", "steganography", "steganographic",
    "collusion", "sabotage",
    "evaluation awareness", "eval awareness",
    "faithfulness", "unfaithful", "safety training", "harmlessness",
    "e-value", "e-values", "test martingale", "martingales",
    "anytime-valid", "conformal prediction",
    "domain shift", "covariate shift", "abstention",
]

EXCLUSION_HORS_CHAMP: list[str] = [
    "asset pricing", "cross-section of expected returns", "factor zoo", "patent citations",
]

SAUVETAGE_SECURITE_STRICTE: list[str] = [
    "jailbreak", "backdoor", "interpretability", "ai control",
    "sparse autoencoder", "reward hacking", "unlearning",
    "sandbagging", "deceptive alignment",
]

NOMS_AXES: dict[str, str] = {
    "AXE_01": "Sondes linéaires et détection interne du mensonge",
    "AXE_02": "Auto-encodeurs épars, superposition et dictionnaires de traits",
    "AXE_03": "Circuits mécanistes et attribution causale interne",
    "AXE_04": "Pilotage d'activations et ingénierie des représentations",
    "AXE_05": "Apprentissage sur retours humains, suroptimisation de récompense et complaisance",
    "AXE_06": "Contournement des garde-fous d'invites et attaques adverses d'entrée",
    "AXE_07": "Classifieurs de garde-fous, modération et entraînement au refus",
    "AXE_08": "Portes dérobées, chevaux de Troie, empoisonnement et agents dormants",
    "AXE_09": "Désapprentissage automatique et résistance au réapprentissage",
    "AXE_10": "Tromperie stratégique, dissimulation de capacités et conscience d'évaluation",
    "AXE_11": "Protocoles de contrôle de l'intelligence artificielle et surveillance de sabotage",
    "AXE_12": "Supervision évolutive, débat contradictoire et juges automatisés",
    "AXE_13": "Fidélité de la chaîne de pensée et raisonnement dissimulé",
    "AXE_14": "Stéganographie algorithmique, filigranage et collusion multi-agents",
    "AXE_15": "Équipes rouges automatisées et recherche adaptative d'attaques",
    "AXE_16": "Audit statistique séquentiel, valeurs de preuve et garanties toujours valides",
    "AXE_17": "Transfert hors domaine et calibration sélective des détecteurs",
    "AXE_18": "Sécurité des agents autonomes et exécution d'outils",
}

AXES: dict[str, list[str]] = {
    "AXE_01": [
        "linear probe", "linear probes", "probing classifier", "lie detector", "lie detection",
        "truth direction", "contrast-consistent search", "mass-mean",
        "internal representations of truth", "honesty probe", "deception probe",
    ],
    "AXE_02": [
        "sparse autoencoder", "sparse autoencoders", "dictionary learning", "superposition",
        "polysemantic", "polysemanticity", "monosemantic", "monosemanticity",
        "feature splitting", "feature absorption", "transcoder",
    ],
    "AXE_03": [
        "mechanistic interpretability", "activation patching", "causal scrubbing",
        "path patching", "attribution patching", "induction head", "induction heads",
        "circuit discovery", "causal mediation", "logit lens", "tuned lens",
    ],
    "AXE_04": [
        "activation steering", "steering vector", "steering vectors", "representation engineering",
        "concept erasure", "leace", "inference-time intervention", "activation addition",
        "contrastive activation", "circuit breakers", "representation rerouting",
    ],
    "AXE_05": [
        "rlhf", "direct preference optimization", "reward model", "reward modeling",
        "reward hacking", "overoptimization", "reward tampering",
        "sycophancy", "sycophantic", "preference learning", "kl penalty",
    ],
    "AXE_06": [
        "jailbreak", "jailbreaking", "jailbreaks", "adversarial suffix", "adversarial suffixes",
        "prompt injection", "gcg", "many-shot jailbreaking", "refusal bypass",
        "adversarial prompt", "cipherchat",
    ],
    "AXE_07": [
        "guardrail", "guardrails", "safety classifier", "constitutional classifier",
        "input filter", "output filter", "refusal training", "safety alignment",
        "harmlessness training", "moderation model", "llama guard",
    ],
    "AXE_08": [
        "backdoor", "backdoors", "trojan", "trojans", "data poisoning",
        "sleeper agent", "sleeper agents", "trigger phrase", "poisoned model",
        "weight poisoning", "clean-label poisoning",
    ],
    "AXE_09": [
        "machine unlearning", "llm unlearning", "unlearning", "capability removal",
        "rmu", "tamper resistance", "tamper-resistant", "benign fine-tuning",
        "relearning attack", "knowledge erasure", "harmful fine-tuning",
    ],
    "AXE_10": [
        "deceptive alignment", "scheming", "sandbagging", "evaluation awareness", "eval awareness",
        "alignment faking", "strategic deception", "situational awareness",
        "capability elicitation", "password-locked", "underperformance",
    ],
    "AXE_11": [
        "ai control", "control protocol", "control protocols", "trusted monitor",
        "trusted monitoring", "untrusted model", "defer-to-trusted", "upfront auditing",
        "code sabotage", "subtle sabotage", "diffuse threat", "safety-usefulness",
    ],
    "AXE_12": [
        "scalable oversight", "ai debate", "weak-to-strong", "llm-as-a-judge", "llm judge",
        "prover-verifier", "amplification", "recursive oversight", "judge model", "automated evaluator",
    ],
    "AXE_13": [
        "chain-of-thought faithfulness", "unfaithful chain-of-thought", "unfaithful reasoning",
        "cot monitoring", "thought monitor", "encoded reasoning", "hidden reasoning",
        "reasoning model", "reasoning trace", "unfaithful explanation",
    ],
    "AXE_14": [
        "steganography", "steganographic", "watermark", "watermarking",
        "covert channel", "covert communication", "collusion", "secret collusion",
        "subliminal", "undetectable covert",
    ],
    "AXE_15": [
        "red-teaming", "automated red", "attacker llm", "adaptive attack", "adaptive attacks",
        "attack success rate", "adversarial testing", "automated adversary", "fuzzing",
    ],
    "AXE_16": [
        "e-value", "e-values", "test martingale", "martingales",
        "sequential test", "sequential testing", "anytime-valid",
        "ville inequality", "confidence sequence", "sequential audit", "betting score",
    ],
    "AXE_17": [
        "domain shift", "covariate shift", "cross-domain", "cross-model",
        "calibration error", "selective classification", "conformal prediction",
        "abstention", "out-of-domain",
    ],
    "AXE_18": [
        "autonomous agent", "autonomous agents", "tool-use", "agent safety",
        "agentic", "computer use", "web agent", "coding agent", "multi-step task", "sandbox",
    ],
}

TENSION: dict[str, list[str]] = {
    "S1": [
        "ad-hoc", "heuristic", "heuristics", "heuristically", "hand-crafted",
        "manually calibrated", "post-hoc patch", "post-hoc heuristic", "post-hoc fix",
        "workaround", "stopgap", "band-aid", "trial-and-error", "empirical trick",
        "sensitive to hyperparameter", "sensitive to the choice of",
        "sensitive to threshold", "sensitive to wording",
        "requires careful tuning", "auxiliary loss", "extra regularization",
    ],
    "S2": [
        "fails to generalize", "fail to generalize", "poor generalization",
        "does not transfer", "do not transfer", "fails to transfer", "fail to transfer",
        "drops sharply", "drops significantly", "drops substantially",
        "breaks down when", "breaks down under",
        "spurious correlation", "spurious correlations", "shortcut learning",
        "clever hans", "overfits to", "overfitting to", "struggles to generalize",
    ],
    "S3": [
        "contradicts prior", "contradicting prior", "contradictory results",
        "in contrast to prior", "in contrast to previous",
        "contrary to common", "contrary to prior", "contrary to popular",
        "mixed results", "inconsistent results", "inconsistent findings", "inconsistent across",
        "fails to replicate", "fail to replicate",
        "remains poorly understood", "remain poorly understood", "lacks consensus",
        "conflicting evidence", "conflicting results", "conflicting findings",
        "puzzling", "anomalous", "anomaly", "anomalies",
        "paradox", "paradoxical", "at odds with",
    ],
    "S4": [
        "fails at scale", "fail at scale", "inverse scaling", "degrades with scale",
        "scaling alone does not", "easily bypassed", "easily circumvented",
        "easily evaded", "easily undone", "easily reversed", "within a few steps",
        "high false-positive rate", "fragility of", "fragile", "brittle", "brittleness",
        "merely superficial", "superficial fix", "obfuscated", "obfuscation",
        "illusion of", "fundamental limitation", "fundamental limitations",
        "lacks formal assurance", "vulnerable to simple", "vulnerable to trivial",
    ],
    "S5": [
        "so-called", "loosely speaking", "abuse of notation", "for lack of a better",
        "ill-defined", "lacks standard definition", "ambiguous definition",
        "conflate", "conflates", "conflating", "entangled with", "entangles",
        "confounded by", "confounded with", "terminological", "dubbed", "what we call",
    ],
}

REFORM: dict[str, list[str]] = {
    "F2": [
        "impossibility theorem", "impossibility result", "prove that no",
        "necessary and sufficient", "minimax",
        "information-theoretic bound", "information-theoretic lower bound",
        "information-theoretic upper bound", "tight lower bound",
        "tight upper bound", "tight bound",
        "game-theoretic equilibrium", "game-theoretic framework", "game-theoretic formulation",
        "nash equilibrium", "stackelberg", "exact characterization", "closed-form",
        "identifiability", "non-identifiable", "non-identifiability",
    ],
    "F3": [
        "unifying framework", "unified framework", "unified theory",
        "unified view", "unified perspective", "unified formulation",
        "formalizes", "formalize the", "formalize a",
        "formal framework", "theoretical framework",
        "disentangle", "disentangles", "disentangling",
        "decouple", "decouples", "decoupling",
        "decomposition into", "decompose into",
        "orthogonality", "orthogonalize", "orthogonalizing",
        "invariance under", "invariant to",
        "canonical decomposition", "canonical form",
        "reformulation", "reformulating", "first-principles",
    ],
}

MOTIF_F1_SENSIBLE_CASSE = re.compile(
    r"(?<![A-Za-z0-9])(?:(?:Theorem|Proposition|Corollary|Definition|Axiom)\s+\d+(?:\.\d+)*"
    r"|Proof(?:\s+of\s+(?:Theorem|Proposition|Lemma|Corollary)(?:\s+[A-Z]?\d+(?:\.\d+)*)?)?\s*[.:])"
)


# ============================================================================
# Compilation d'expressions régulières et gardes R5 (n° 1 et n° 2)
# ============================================================================

def compiler_union_termes(termes: list[str]) -> re.Pattern[str]:
    """Compile une liste de termes en une union unique triée par longueur décroissante (section 1)."""
    if not termes:
        raise ErreurGardeRang1("Liste de termes vide interdite.")
    motifs: list[str] = []
    for t in sorted(set(termes), key=len, reverse=True):
        echappe = re.escape(t)
        echappe = echappe.replace(r"\ ", r"\s+").replace(r"\-", r"[- ]?")
        motifs.append(echappe)
    return re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(motifs) + r")(?![A-Za-z0-9])", re.IGNORECASE)


def compter_disjoint(rx: re.Pattern[str], texte: str) -> int:
    """Renvoie le nombre de correspondances disjointes de gauche à droite."""
    return len(rx.findall(texte))


def compter_et_detailler(rx: re.Pattern[str], texte: str) -> tuple[int, dict[str, int]]:
    """Renvoie le comptage disjoint et la ventilation normalisée par correspondance trouvée."""
    trouves = rx.findall(texte)
    detail: dict[str, int] = {}
    for m in trouves:
        cle = re.sub(r"[\s-]+", " ", m.lower()).strip()
        detail[cle] = detail.get(cle, 0) + 1
    return len(trouves), detail


def verifier_prereg_scelle(
    chemin_prereg: str | Path,
    empreinte_attendue: str | None = EMPREINTE_PREREG_ATTENDUE,
) -> str:
    """Garde d'arrêt n° 1 : vérifie la conformité R1/R2 et l'empreinte scellée avant exécution."""
    try:
        sha = exiger_prereg_scelle(chemin_prereg)
    except GardeArret as exc:
        raise ErreurGardeRang1(f"Garde n° 1 déclenchée (préenregistrement invalide ou non scellé) : {exc}") from exc
    if empreinte_attendue is not None and sha != empreinte_attendue:
        raise ErreurGardeRang1(
            f"Garde n° 1 déclenchée : empreinte {sha} différente de l'empreinte attendue {empreinte_attendue}"
        )
    return sha


def verifier_orthogonalite_lexicale(
    axes: dict[str, list[str]] = AXES,
    tension: dict[str, list[str]] = TENSION,
    reform: dict[str, list[str]] = REFORM,
    rx_f1: re.Pattern[str] = MOTIF_F1_SENSIBLE_CASSE,
) -> None:
    """Garde d'arrêt n° 2 : vérifie les six directions ordonnées, les suffixes-préfixes et les sous-groupes."""
    termes_axes = [t for lst in axes.values() for t in lst]
    termes_tension = [t for lst in tension.values() for t in lst]
    termes_reform = [t for lst in reform.values() for t in lst]
    temoins_f1 = ["Theorem 1", "Proposition 2.1", "Corollary 3", "Definition 1.2", "Axiom 1", "Proof.", "Proof of Theorem 1."]

    rx_axes = compiler_union_termes(termes_axes)
    rx_tens = compiler_union_termes(termes_tension)
    rx_ref_f23 = compiler_union_termes(termes_reform)

    vocs_temoins: dict[str, list[str]] = {
        "axes": termes_axes,
        "tension": termes_tension,
        "reform": termes_reform + temoins_f1,
    }
    vocs_termes: dict[str, list[str]] = {
        "axes": termes_axes,
        "tension": termes_tension,
        "reform": termes_reform,
    }
    detecteurs = {
        "axes": lambda s: bool(rx_axes.search(s)),
        "tension": lambda s: bool(rx_tens.search(s)),
        "reform": lambda s: bool(rx_ref_f23.search(s) or rx_f1.search(s)),
    }

    for k1, lst1 in vocs_temoins.items():
        for k2 in vocs_temoins:
            if k1 == k2:
                continue
            for t in lst1:
                for variante in (t, t.replace("-", " "), t.replace("-", "")):
                    if detecteurs[k2](variante):
                        raise ErreurGardeRang1(
                            f"Garde n° 2 déclenchée : correspondance directe {k1} -> {k2} sur {variante!r}"
                        )

    for k1, lst1 in vocs_termes.items():
        for k2, lst2 in vocs_termes.items():
            if k1 == k2:
                continue
            for t1 in lst1:
                w1 = re.findall(r"[a-z0-9]+", t1.lower())
                for t2 in lst2:
                    w2 = re.findall(r"[a-z0-9]+", t2.lower())
                    for lg in range(1, min(len(w1), len(w2)) + 1):
                        if w1[-lg:] == w2[:lg]:
                            raise ErreurGardeRang1(
                                f"Garde n° 2 déclenchée : recouvrement suffixe-préfixe entre {k1}({t1!r}) et {k2}({t2!r})"
                            )

    for a1, l1 in axes.items():
        r1 = compiler_union_termes(l1)
        for a2, l2 in axes.items():
            if a1 == a2:
                continue
            for t in l2:
                if r1.search(t):
                    raise ErreurGardeRang1(f"Garde n° 2 déclenchée : inclusion inter-axes {a2}({t!r}) -> {a1}")

    for s1, l1 in tension.items():
        r1 = compiler_union_termes(l1)
        for s2, l2 in tension.items():
            if s1 == s2:
                continue
            for t in l2:
                if r1.search(t):
                    raise ErreurGardeRang1(f"Garde n° 2 déclenchée : inclusion inter-composantes {s2}({t!r}) -> {s1}")

    for f1_k, l1 in reform.items():
        r1 = compiler_union_termes(l1)
        for f2_k, l2 in reform.items():
            if f1_k == f2_k:
                continue
            for t in l2:
                if r1.search(t):
                    raise ErreurGardeRang1(f"Garde n° 2 déclenchée : inclusion inter-reform {f2_k}({t!r}) -> {f1_k}")


# ============================================================================
# Prétraitement canonique, datation et extraction PDF (section 2)
# ============================================================================

_RX_ARXIV_MOD = re.compile(r"(?<![0-9])(([0-2][0-9])(0[1-9]|1[0-2])\.[0-9]{4,5})(?:v(\d+))?(?![0-9])")
_RX_ARXIV_OLD = re.compile(
    r"((?:math|cs|stat|physics|cond-mat|quant-ph|hep-th)[-_]?([09][0-9])(0[1-9]|1[0-2])[0-9]{3})(?:v(\d+))?",
    re.IGNORECASE,
)
_RX_ANNEE_NOM = re.compile(r"(?<!\d)(19[2-9][0-9]|20[0-2][0-9])(?!\d)")
_RX_REFS = re.compile(r"^\s*(?:\d+\.?\s+)?(?:References|Bibliography|REFERENCES|BIBLIOGRAPHY)\s*$", re.MULTILINE)
_RX_MOTS = re.compile(r"[A-Za-z]{3,}")
_RX_CESURE = re.compile(r"([a-z])-\r?\n\s*([a-z])")
_RX_PROSPECTIF = re.compile(r"\b(?:by|until|before|beyond)\s+(?:19[89]\d|20[0-2]\d)\b", re.IGNORECASE)
_RX_ANNEE_ENTETE = re.compile(r"(?<!\d)(19[89][0-9]|20[0-2][0-6])(?!\d)")
_RX_MASQUE_ID_ARXIV = re.compile(r"arXiv:\s*\d{4}\.\d{4,5}", re.IGNORECASE)
_RX_REV_25_26 = re.compile(r"\b202[56]\b")

_TABLE_LIGATURES = str.maketrans({
    "\ufb01": "fi",
    "\ufb02": "fl",
    "\ufb00": "ff",
    "\ufb03": "ffi",
    "\ufb04": "ffl",
    "\u2013": "-",
    "\u2014": "-",
    "\u2212": "-",
    "\u2018": "'",
    "\u2019": "'",
})


def empreinte_sha256_fichier(chemin: Path) -> str:
    """Lit l'empreinte compagnon `.sha256` si présente, sinon calcule le SHA-256 binaire."""
    comp = Path(str(chemin) + ".sha256")
    if comp.is_file():
        premier = comp.read_text(encoding="utf-8").strip().split()[0]
        if re.fullmatch(r"[0-9a-f]{64}", premier):
            return premier
    h = hashlib.sha256()
    with open(chemin, "rb") as f:
        for bloc in iter(lambda: f.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def identifier_cle_et_millesime_nominal(rel_path: str, sha256: str) -> tuple[str, int | None, float, str]:
    """Détermine la clé canonique, le millésime nominal (si présent), le rang de version et la source."""
    nom = Path(rel_path).name
    m_mod = _RX_ARXIV_MOD.search(nom)
    if m_mod:
        yy = int(m_mod.group(2))
        if 7 <= yy <= 26:
            rang_v = float(int(m_mod.group(4))) if m_mod.group(4) is not None else 1.5
            return f"arxiv:{m_mod.group(1)}", 2000 + yy, rang_v, "arxiv_moderne"

    m_old = _RX_ARXIV_OLD.search(nom)
    if m_old:
        yy = int(m_old.group(2))
        annee = 1900 + yy if yy >= 91 else 2000 + yy
        rang_v = float(int(m_old.group(4))) if m_old.group(4) is not None else 1.5
        base = re.sub(r"[-_]", "", m_old.group(1).lower())
        return f"oldarxiv:{base}", annee, rang_v, "arxiv_ancien"

    cle = f"sha256:{sha256}"
    m4 = _RX_ANNEE_NOM.findall(nom)
    if m4:
        return cle, int(m4[0]), 1.5, "nom_fichier_yyyy"

    nom_bas = nom.lower()
    if "usenixsecurity23" in nom_bas:
        return cle, 2023, 1.5, "code_acte"
    if "pmlr-v306" in nom_bas or "wei26s" in nom_bas or "yulong26a" in nom_bas:
        return cle, 2026, 1.5, "code_acte"
    if "nber-w20592" in nom_bas:
        return cle, 2014, 1.5, "code_cahier"
    if "nber-w22180" in nom_bas:
        return cle, 2016, 1.5, "code_cahier"
    if "nber-w25481" in nom_bas:
        return cle, 2019, 1.5, "code_cahier"

    return cle, None, 1.5, "entete_requise"


def inferer_millesime_entete(texte_debut: str) -> int | None:
    """Règle (c) section 2.1 : maximum des millésimes 1980-2026 hors mentions prospectives."""
    propre = _RX_PROSPECTIF.sub(" ", texte_debut[:2000])
    annees = [int(a) for a in _RX_ANNEE_ENTETE.findall(propre)]
    return max(annees) if annees else None


def normaliser_et_decouper_texte(flux_brut: str, annee: int | None) -> dict[str, Any]:
    """Applique la normalisation des ligatures, la détection post-2024 et le découpage hors bibliographie."""
    flux = flux_brut.translate(_TABLE_LIGATURES)
    flux = _RX_CESURE.sub(r"\1\2", flux)
    w_brut = len(_RX_MOTS.findall(flux))

    revision_post_2024 = False
    if annee is not None and annee <= 2024:
        entete_masquee = _RX_MASQUE_ID_ARXIV.sub(" ", flux[:1500])
        if _RX_REV_25_26.search(entete_masquee):
            revision_post_2024 = True

    seuil_pos = int(math.ceil(0.35 * len(flux)))
    coupure = None
    for m in _RX_REFS.finditer(flux):
        if m.start() >= seuil_pos:
            coupure = m.start()
            break

    if coupure is not None:
        corps_brut = flux[:coupure]
        biblio_tronquee = True
    else:
        corps_brut = flux[:65000]
        biblio_tronquee = False

    corps_principal = re.sub(r"\s+", " ", corps_brut).strip()
    ouverture = corps_principal[:6000]
    w_corps = len(_RX_MOTS.findall(corps_principal))

    return {
        "w_brut": w_brut,
        "w_corps": w_corps,
        "revision_post_2024": revision_post_2024,
        "biblio_tronquee": biblio_tronquee,
        "corps_principal": corps_principal,
        "ouverture": ouverture,
    }


def appeler_pdftotext(chemin_pdf: Path) -> tuple[bool, str]:
    """Extrait le flux UTF-8 d'un fichier PDF via `/usr/bin/pdftotext`."""
    try:
        proc = subprocess.run(
            ["/usr/bin/pdftotext", "-enc", "UTF-8", "-q", str(chemin_pdf), "-"],
            capture_output=True,
            timeout=45,
            check=False,
        )
    except Exception as exc:
        return False, f"exception:{type(exc).__name__}"
    if proc.returncode != 0:
        return False, f"returncode:{proc.returncode}"
    try:
        texte = proc.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return False, "decode_error"
    return True, texte


def inventorier_et_dedoublonner_pdfs(racine_pdf: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Parcourt `racine_pdf` et applique le dédoublonnage canonique exact de la section 2.1."""
    tous_pdfs = sorted(racine_pdf.rglob("*.pdf"))
    groupes: dict[str, list[dict[str, Any]]] = {}
    for p in tous_pdfs:
        rel = str(p.relative_to(racine_pdf))
        sha = empreinte_sha256_fichier(p)
        cle, annee, rang_v, src = identifier_cle_et_millesime_nominal(rel, sha)
        groupes.setdefault(cle, []).append({
            "cle_canonique": cle,
            "chemin_absolu": str(p),
            "chemin_relatif": rel,
            "sha256": sha,
            "annee_nominale": annee,
            "rang_version": rang_v,
            "source_annee": src,
        })

    retenus: list[dict[str, Any]] = []
    doublons_ecartes = 0
    for cle in sorted(groupes.keys()):
        candidats = groupes[cle]
        annee_ref = candidats[0]["annee_nominale"]
        if annee_ref is not None and annee_ref <= 2024:
            choisi = min(candidats, key=lambda c: (c["rang_version"], c["chemin_relatif"]))
        elif annee_ref is not None and annee_ref >= 2025:
            choisi = min(candidats, key=lambda c: (-c["rang_version"], c["chemin_relatif"]))
        else:
            choisi = min(candidats, key=lambda c: c["chemin_relatif"])
        doublons_ecartes += len(candidats) - 1
        retenus.append(choisi)

    resume_inv = {
        "fichiers_pdf_totaux": len(tous_pdfs),
        "documents_canoniques_uniques": len(retenus),
        "doublons_ou_versions_ecartes": doublons_ecartes,
    }
    return retenus, resume_inv


# ============================================================================
# Analyse documentaire unitaire (éligibilité, axes, scores bruts S et F)
# ============================================================================

class AnalyseurLexicalCompile:
    """Regroupe les expressions régulières précompilées des sections 3 à 6."""

    def __init__(self) -> None:
        self.rx_ancrage_mod = compiler_union_termes(ANCRAGE_MODELES)
        self.rx_ancrage_ctrl = compiler_union_termes(ANCRAGE_CONTROLE)
        self.rx_excl_hors = compiler_union_termes(EXCLUSION_HORS_CHAMP)
        self.rx_sauvetage = compiler_union_termes(SAUVETAGE_SECURITE_STRICTE)
        self.rx_axes = {k: compiler_union_termes(v) for k, v in AXES.items()}
        self.rx_tension = {k: compiler_union_termes(v) for k, v in TENSION.items()}
        self.rx_reform_f23 = {k: compiler_union_termes(v) for k, v in REFORM.items()}
        self.rx_f1 = MOTIF_F1_SENSIBLE_CASSE

    def analyser_document(self, entree: dict[str, Any], flux_brut: str) -> dict[str, Any]:
        annee = entree["annee_nominale"]
        source_annee = entree["source_annee"]
        if annee is None:
            flux_temp = flux_brut[:3000].translate(_TABLE_LIGATURES)
            annee = inferer_millesime_entete(flux_temp)
            source_annee = "entete_max_millesime" if annee is not None else "introuvable"

        decoupe = normaliser_et_normaliser_doc(flux_brut, annee)
        ouv = decoupe["ouverture"]
        corps = decoupe["corps_principal"]
        w_brut = decoupe["w_brut"]
        w_corps = decoupe["w_corps"]

        # Éligibilité thématique (section 3)
        n_mod = compter_disjoint(self.rx_ancrage_mod, ouv)
        n_ctrl = compter_disjoint(self.rx_ancrage_ctrl, ouv)
        n_hors = compter_disjoint(self.rx_excl_hors, ouv)
        n_sauv = compter_disjoint(self.rx_sauvetage, ouv)

        annee_valide = annee is not None and 1980 <= annee <= 2026
        mots_valides = w_brut >= 250 and w_corps >= 250
        hors_champ_bloque = (n_hors > 0) and (n_sauv == 0)
        eligible_thematique = (
            annee_valide
            and mots_valides
            and (n_mod >= 1)
            and (n_ctrl >= 2)
            and (not hors_champ_bloque)
        )

        # Affinités aux 18 sous-domaines (section 4)
        axes_actifs: list[str] = []
        scores_axes: dict[str, int] = {}
        meilleur_tuple: tuple[int, int, int, int, int] | None = None
        axe_primaire: str | None = None

        if eligible_thematique and w_corps > 0:
            for idx_k, code_axe in enumerate(sorted(self.rx_axes.keys()), start=1):
                rx_a = self.rx_axes[code_axe]
                c_ouv = compter_disjoint(rx_a, ouv)
                c_corps_brut = compter_disjoint(rx_a, corps)
                c_corps = min(20, c_corps_brut)
                s_axe = 3 * c_ouv + c_corps
                scores_axes[code_axe] = s_axe
                if c_ouv >= 1 and s_axe >= 5:
                    axes_actifs.append(code_axe)
                if s_axe >= 4:
                    m_first = rx_a.search(corps)
                    pos_first = m_first.start() if m_first else len(corps)
                    cle_tri = (s_axe, 3 * c_ouv + c_corps_brut, c_ouv, -pos_first, -idx_k)
                    if meilleur_tuple is None or cle_tri > meilleur_tuple:
                        meilleur_tuple = cle_tri
                        axe_primaire = code_axe

        # Densités S1..S5 et F1..F3 (sections 5 et 6)
        densites_s: dict[str, float] = {}
        details_termes_s: dict[str, int] = {}
        densites_f: dict[str, float] = {}
        details_termes_f: dict[str, int] = {}

        if w_corps > 0:
            facteur = 1000.0 / float(w_corps)
            for nom_s, rx_s in self.rx_tension.items():
                cnt, det = compter_et_detailler(rx_s, corps)
                densites_s[nom_s] = cnt * facteur
                for k_t, v_t in det.items():
                    details_termes_s[k_t] = details_termes_s.get(k_t, 0) + v_t

            cnt_f1 = len(self.rx_f1.findall(corps))
            densites_f["F1"] = min(15.0, cnt_f1 * facteur)
            if cnt_f1 > 0:
                details_termes_f["F1_enonces_et_preuves"] = cnt_f1

            cnt_f2, det_f2 = compter_et_detailler(self.rx_reform_f23["F2"], corps)
            densites_f["F2"] = cnt_f2 * facteur
            for k_t, v_t in det_f2.items():
                details_termes_f[k_t] = details_termes_f.get(k_t, 0) + v_t

            cnt_f3_corps, det_f3 = compter_et_detailler(self.rx_reform_f23["F3"], corps)
            cnt_f3_ouv = compter_disjoint(self.rx_reform_f23["F3"], ouv)
            densites_f["F3"] = (cnt_f3_corps + cnt_f3_ouv) * facteur
            for k_t, v_t in det_f3.items():
                details_termes_f[k_t] = details_termes_f.get(k_t, 0) + v_t
        else:
            for nom_s in self.rx_tension:
                densites_s[nom_s] = 0.0
            for nom_f in ("F1", "F2", "F3"):
                densites_f[nom_f] = 0.0

        titre_court = extraire_titre_approximatif(ouv, entree["chemin_relatif"])

        return {
            "cle_canonique": entree["cle_canonique"],
            "chemin_relatif": entree["chemin_relatif"],
            "sha256": entree["sha256"],
            "annee": annee,
            "source_annee": source_annee,
            "rang_version": entree["rang_version"],
            "w_brut": w_brut,
            "w_corps": w_corps,
            "biblio_tronquee": decoupe["biblio_tronquee"],
            "revision_post_2024": decoupe["revision_post_2024"],
            "eligible_thematique_hors_filtre_rev": eligible_thematique,
            "eligible_primaire": eligible_thematique and not (
                annee is not None and annee <= 2024 and decoupe["revision_post_2024"]
            ),
            "axes_actifs": axes_actifs,
            "axe_primaire": axe_primaire,
            "scores_axes": scores_axes,
            "densites_s": densites_s,
            "densites_f": densites_f,
            "details_termes_s": details_termes_s,
            "details_termes_f": details_termes_f,
            "titre_extrait": titre_court,
        }


def normaliser_et_normaliser_doc(flux_brut: str, annee: int | None) -> dict[str, Any]:
    return normaliser_et_decouper_texte(flux_brut, annee)


def extraire_titre_approximatif(ouverture: str, fallback: str) -> str:
    extrait = ouverture[:180].strip()
    return extrait if extrait else fallback


# ============================================================================
# Fonctions statistiques exactes (sections 5, 6, 7, 8 et gardes n° 4 et n° 5)
# ============================================================================

def aire_sous_courbe_exacte(scores: np.ndarray, cibles: np.ndarray) -> float:
    """Calcule l'aire sous la courbe caractéristique de réception par Mann-Whitney avec demi-poids 0,5."""
    scores_arr = np.asarray(scores, dtype=float)
    cibles_arr = np.asarray(cibles, dtype=int)
    pos = scores_arr[cibles_arr == 1]
    neg = scores_arr[cibles_arr == 0]
    if len(pos) == 0 or len(neg) == 0:
        raise ValueError("Les deux classes 0 et 1 doivent être non vides pour calculer A(X, Z).")
    diff = pos[:, None] - neg[None, :]
    victoires = np.sum(diff > 0.0) + 0.5 * np.sum(diff == 0.0)
    return float(victoires / (len(pos) * len(neg)))


def spearman_exact(x: np.ndarray, y: np.ndarray) -> float:
    """Corrélation linéaire de Pearson sur les rangs moyens demi-entiers (0,0 si variance nulle)."""
    rx = stats.rankdata(np.asarray(x, dtype=float), method="average")
    ry = stats.rankdata(np.asarray(y, dtype=float), method="average")
    sx = rx - np.mean(rx)
    sy = ry - np.mean(ry)
    denom = float(np.linalg.norm(sx) * np.linalg.norm(sy))
    if denom < 1e-12:
        return 0.0
    return float(np.dot(sx, sy) / denom)


def spearman_partiel_exact(u: np.ndarray, v_cible: np.ndarray, w_cov: np.ndarray) -> float:
    """Section 8.4 : Pearson entre les résidus MCO (avec constante) sur les rangs moyens."""
    ru = stats.rankdata(np.asarray(u, dtype=float), method="average")
    rv = stats.rankdata(np.asarray(v_cible, dtype=float), method="average")
    w_arr = np.asarray(w_cov, dtype=float)
    if w_arr.ndim == 1:
        w_arr = w_arr[:, None]
    rw_cols = [stats.rankdata(w_arr[:, j], method="average") for j in range(w_arr.shape[1])]
    design = np.column_stack([np.ones(len(ru), dtype=float), *rw_cols])

    coef_u, _, _, _ = np.linalg.lstsq(design, ru, rcond=None)
    coef_v, _, _, _ = np.linalg.lstsq(design, rv, rcond=None)
    res_u = ru - design @ coef_u
    res_v = rv - design @ coef_v

    res_u_c = res_u - np.mean(res_u)
    res_v_c = res_v - np.mean(res_v)
    norm_u = float(np.linalg.norm(res_u_c))
    norm_v = float(np.linalg.norm(res_v_c))
    if norm_u < 1e-12 or norm_v < 1e-12:
        return 0.0
    return float(np.dot(res_u_c, res_v_c) / (norm_u * norm_v))


def binariser_mediane_avec_repli(valeurs: np.ndarray) -> tuple[np.ndarray, float, str]:
    """Section 6 : indicateur > médiane, avec repli déterministe vers >= médiane si plateau au sommet."""
    arr = np.asarray(valeurs, dtype=float)
    med = float(np.median(arr))
    if np.allclose(arr, arr[0], atol=1e-15):
        return np.zeros(len(arr), dtype=int), med, "constant_degenere"
    strict = (arr > med).astype(int)
    if int(np.sum(strict)) == 0:
        large = (arr >= med).astype(int)
        return large, med, "repli_superieur_ou_egal_plateau"
    return strict, med, "strictement_superieur_mediane"


def p_permutation_spearman(
    x: np.ndarray,
    y: np.ndarray,
    rng: np.random.Generator,
    n_perm: int = 10_000,
) -> tuple[float, float]:
    """Section 8.2 : valeur-p unilatérale supérieure exacte de Monte-Carlo sur 10 000 permutations."""
    obs = spearman_exact(x, y)
    rx = stats.rankdata(x, method="average")
    ry = stats.rankdata(y, method="average")
    sx = rx - np.mean(rx)
    norm_sx = float(np.linalg.norm(sx))
    sy_base = ry - np.mean(ry)
    norm_sy = float(np.linalg.norm(sy_base))
    if norm_sx < 1e-12 or norm_sy < 1e-12:
        return obs, 1.0

    denom = norm_sx * norm_sy
    n = len(ry)
    mat_sy = np.empty((n_perm, n), dtype=float)
    for b in range(n_perm):
        mat_sy[b] = sy_base[rng.permutation(n)]
    rhos_b = (mat_sy @ sx) / denom
    sup_ou_egal = int(np.sum(rhos_b >= obs - 1e-15))
    return obs, float((1 + sup_ou_egal) / (n_perm + 1))


def intervalle_auc_reechantillonnage(
    x: np.ndarray,
    z: np.ndarray,
    rng: np.random.Generator,
    n_rep: int = 10_000,
) -> dict[str, Any]:
    """Section 8.1 : intervalle 2,5 %-97,5 % par rééchantillonnage avec remise stratifié."""
    idx_pos = np.where(z == 1)[0]
    idx_neg = np.where(z == 0)[0]
    if len(idx_pos) == 0 or len(idx_neg) == 0:
        return {"ic95_bas": None, "ic95_haut": None, "singleton_strate": True, "ic95_non_stratifie": None}

    vals_strat = np.empty(n_rep, dtype=float)
    for b in range(n_rep):
        s_pos = rng.choice(idx_pos, size=len(idx_pos), replace=True)
        s_neg = rng.choice(idx_neg, size=len(idx_neg), replace=True)
        x_b = np.concatenate([x[s_pos], x[s_neg]])
        z_b = np.concatenate([np.ones(len(s_pos), dtype=int), np.zeros(len(s_neg), dtype=int)])
        vals_strat[b] = aire_sous_courbe_exacte(x_b, z_b)

    singleton = min(len(idx_pos), len(idx_neg)) == 1
    ic_non_strat = None
    if singleton:
        vals_ns: list[float] = []
        essais = 0
        while len(vals_ns) < n_rep and essais < n_rep * 5:
            essais += 1
            tir = rng.choice(len(x), size=len(x), replace=True)
            z_t = z[tir]
            if 0 < int(np.sum(z_t)) < len(z_t):
                vals_ns.append(aire_sous_courbe_exacte(x[tir], z_t))
        if vals_ns:
            ic_non_strat = [float(np.percentile(vals_ns, 2.5)), float(np.percentile(vals_ns, 97.5))]

    return {
        "ic95_bas": float(np.percentile(vals_strat, 2.5)),
        "ic95_haut": float(np.percentile(vals_strat, 97.5)),
        "singleton_strate": singleton,
        "ic95_non_stratifie": ic_non_strat,
    }


def verifier_temoin_nul_doit_mourir(
    x: np.ndarray,
    y_taux: np.ndarray,
    rng: np.random.Generator,
    n_sim: int = 2_000,
    n_perm_interne: int = 400,
) -> dict[str, float]:
    """Garde d'arrêt n° 5 : témoin nul par permutation de Y_taux sur 2 000 simulations."""
    if np.allclose(x, x[0], atol=1e-15) or np.allclose(y_taux, y_taux[0], atol=1e-15):
        return {"applicable": 0.0, "auc_moyenne_nul": 0.5, "taux_erreur_premiere_espece": 0.0}

    aucs = np.empty(n_sim, dtype=float)
    rejets = 0
    n = len(y_taux)
    for s in range(n_sim):
        y_perm = y_taux[rng.permutation(n)]
        z_perm, _, mode_z = binariser_mediane_avec_repli(y_perm)
        if mode_z == "constant_degenere":
            aucs[s] = 0.5
            continue
        aucs[s] = aire_sous_courbe_exacte(x, z_perm)
        _, p_s = p_permutation_spearman(x, y_perm, rng, n_perm=n_perm_interne)
        if p_s <= 0.05:
            rejets += 1

    auc_moy = float(np.mean(aucs))
    taux_err = float(rejets / n_sim)
    if not (0.47 <= auc_moy <= 0.53):
        raise ErreurGardeRang1(
            f"Garde n° 5 déclenchée (témoin nul doit mourir) : moyenne A(X, Z) sous H0 = {auc_moy:.4f} hors [0,47 ; 0,53]"
        )
    if taux_err > 0.070:
        raise ErreurGardeRang1(
            f"Garde n° 5 déclenchée (témoin nul doit mourir) : taux empirique d'erreur de 1re espèce = {taux_err:.4f} > 0,070"
        )
    return {
        "applicable": 1.0,
        "auc_moyenne_nul": auc_moy,
        "taux_erreur_premiere_espece": taux_err,
    }


def normaliser_scores_tranche(
    docs: list[dict[str, Any]],
    champ_densites: str,
    cles_comp: tuple[str, ...],
) -> tuple[dict[str, float], dict[str, tuple[float, float]]]:
    """Calcule les cotes Z tronquées [-3, +5] avec ddof=0 sur `docs`."""
    params: dict[str, tuple[float, float]] = {}
    for c in cles_comp:
        vals = np.array([d[champ_densites][c] for d in docs], dtype=float)
        mu = float(np.mean(vals)) if len(vals) > 0 else 0.0
        sd = float(np.std(vals, ddof=0)) if len(vals) > 0 else 0.0
        params[c] = (mu, sd)

    scores: dict[str, float] = {}
    for d in docs:
        zs: list[float] = []
        for c in cles_comp:
            mu, sd = params[c]
            if sd == 0.0:
                zs.append(0.0)
            else:
                z = (d[champ_densites][c] - mu) / sd
                zs.append(float(np.clip(z, -3.0, 5.0)))
        scores[d["cle_canonique"]] = float(np.mean(zs))
    return scores, params


def ajuster_benjamini_hochberg(p_vals: list[float]) -> list[float]:
    """Ajustement de multiplicité de Benjamini-Hochberg."""
    m = len(p_vals)
    if m == 0:
        return []
    ordre = np.argsort(p_vals)
    q_vals = np.empty(m, dtype=float)
    courant = 1.0
    for rang_inv in range(m - 1, -1, -1):
        idx = ordre[rang_inv]
        val = p_vals[idx] * m / float(rang_inv + 1)
        courant = min(courant, val)
        q_vals[idx] = min(1.0, courant)
    return [float(x) for x in q_vals]


# ============================================================================
# Orchestration complète de l'évaluation préenregistrée (sections 5 à 8)
# ============================================================================

def evaluer_protocole_sur_documents(
    docs_analyses: list[dict[str, Any]],
    graine: int = GRAINE_MAITRESSE,
    inclure_revisions_post_2024: bool = False,
    mode_assignation_exclusive: bool = False,
    seuil_n_min_axe: int = 3,
    executer_gardes_4_et_5: bool = True,
) -> dict[str, Any]:
    """Exécute le calcul complet (primaire ou variante secondaire préenregistrée)."""
    ss = np.random.SeedSequence(graine)
    flux_rng = [np.random.default_rng(s) for s in ss.spawn(5)]

    champ_elig = "eligible_thematique_hors_filtre_rev" if inclure_revisions_post_2024 else "eligible_primaire"
    elig_amont = [d for d in docs_analyses if d[champ_elig] and d["annee"] is not None and d["annee"] <= 2024]
    elig_aval = [d for d in docs_analyses if d[champ_elig] and d["annee"] is not None and 2025 <= d["annee"] <= 2026]

    def axes_du_doc(d: dict[str, Any]) -> list[str]:
        if mode_assignation_exclusive:
            return [d["axe_primaire"]] if d["axe_primaire"] is not None else []
        return list(d["axes_actifs"])

    nb_rattaches_amont = sum(1 for d in elig_amont if len(axes_du_doc(d)) > 0)
    nb_rattaches_aval = sum(1 for d in elig_aval if len(axes_du_doc(d)) > 0)

    if executer_gardes_4_et_5:
        if len(elig_amont) < 40 or len(elig_aval) < 40:
            raise ErreurGardeRang1(
                f"Garde n° 4 déclenchée : effectifs éligibles insuffisants "
                f"(amont={len(elig_amont)}, aval={len(elig_aval)}, minimum requis=40)"
            )
        if nb_rattaches_amont < 30 or nb_rattaches_aval < 30:
            raise ErreurGardeRang1(
                f"Garde n° 4 déclenchée : documents rattachés à au moins un axe insuffisants "
                f"(amont={nb_rattaches_amont}, aval={nb_rattaches_aval}, minimum requis=30)"
            )

    cles_s = ("S1", "S2", "S3", "S4", "S5")
    cles_f = ("F1", "F2", "F3")
    scores_t_amont, params_s_amont = normaliser_scores_tranche(elig_amont, "densites_s", cles_s)
    scores_r_aval, params_f_aval = normaliser_scores_tranche(elig_aval, "densites_f", cles_f)

    if executer_gardes_4_et_5:
        nb_sd_nuls_s = sum(1 for _, sd in params_s_amont.values() if sd == 0.0)
        nb_sd_nuls_f = sum(1 for _, sd in params_f_aval.values() if sd == 0.0)
        if nb_sd_nuls_s > 2:
            raise ErreurGardeRang1(f"Garde n° 4 déclenchée : {nb_sd_nuls_s}/5 composantes de T ont un écart type nul.")
        if nb_sd_nuls_f == 3:
            raise ErreurGardeRang1("Garde n° 4 déclenchée : les 3 composantes de R ont un écart type nul.")

    # Quantile 0,75 sur R aval et indicateur Percee(d')
    vals_r_aval = np.array([scores_r_aval[d["cle_canonique"]] for d in elig_aval], dtype=float)
    q75_aval = float(np.quantile(vals_r_aval, 0.75, method="linear")) if len(vals_r_aval) > 0 else 0.0
    percee_aval: dict[str, int] = {}
    for d in elig_aval:
        cle = d["cle_canonique"]
        somme_f = d["densites_f"]["F1"] + d["densites_f"]["F2"] + d["densites_f"]["F3"]
        percee_aval[cle] = int(scores_r_aval[cle] >= q75_aval - 1e-15 and somme_f > 0.0)

    # Covariable amont sans fuite Y_k^{taux, <=2024} et R normalisé sur amont
    scores_r_amont_interne, params_f_amont = normaliser_scores_tranche(elig_amont, "densites_f", cles_f)
    vals_r_amont = np.array([scores_r_amont_interne[d["cle_canonique"]] for d in elig_amont], dtype=float)
    q75_amont = float(np.quantile(vals_r_amont, 0.75, method="linear")) if len(vals_r_amont) > 0 else 0.0
    percee_amont: dict[str, int] = {}
    for d in elig_amont:
        cle = d["cle_canonique"]
        somme_f = d["densites_f"]["F1"] + d["densites_f"]["F2"] + d["densites_f"]["F3"]
        percee_amont[cle] = int(scores_r_amont_interne[cle] >= q75_amont - 1e-15 and somme_f > 0.0)

    # Score R aval projeté sur les paramètres amont pour Delta R_k (analyse secondaire a)
    scores_r_aval_base_amont: dict[str, float] = {}
    for d in elig_aval:
        zs_proj = []
        for c in cles_f:
            mu_a, sd_a = params_f_amont[c]
            zs_proj.append(0.0 if sd_a == 0.0 else float(np.clip((d["densites_f"][c] - mu_a) / sd_a, -3.0, 5.0)))
        scores_r_aval_base_amont[d["cle_canonique"]] = float(np.mean(zs_proj))

    # Regroupement par sous-domaine
    par_axe_amont: dict[str, list[dict[str, Any]]] = {k: [] for k in sorted(AXES.keys())}
    par_axe_aval: dict[str, list[dict[str, Any]]] = {k: [] for k in sorted(AXES.keys())}
    for d in elig_amont:
        for k in axes_du_doc(d):
            par_axe_amont[k].append(d)
    for d in elig_aval:
        for k in axes_du_doc(d):
            par_axe_aval[k].append(d)

    axes_eligibles = [
        k for k in sorted(AXES.keys())
        if len(par_axe_amont[k]) >= seuil_n_min_axe and len(par_axe_aval[k]) >= seuil_n_min_axe
    ]
    k_elig = len(axes_eligibles)

    table_axes: list[dict[str, Any]] = []
    for k in sorted(AXES.keys()):
        da = par_axe_amont[k]
        dv = par_axe_aval[k]
        est_elig = k in axes_eligibles
        x_k = float(np.mean([scores_t_amont[d["cle_canonique"]] for d in da])) if da else None
        v_k = len(da)
        v_aval_k = len(dv)
        age_k = float(2024.0 - np.mean([float(d["annee"]) for d in da])) if da else None
        y_taux_k = float(np.mean([percee_aval[d["cle_canonique"]] for d in dv])) if dv else None
        y_taux_amont_k = float(np.mean([percee_amont[d["cle_canonique"]] for d in da])) if da else None
        r_moy_amont = float(np.mean([scores_r_amont_interne[d["cle_canonique"]] for d in da])) if da else None
        r_moy_aval_proj = float(np.mean([scores_r_aval_base_amont[d["cle_canonique"]] for d in dv])) if dv else None
        delta_r_k = (r_moy_aval_proj - r_moy_amont) if (r_moy_aval_proj is not None and r_moy_amont is not None) else None

        comp_s_axe = {}
        for cs in cles_s:
            mu_s, sd_s = params_s_amont[cs]
            if da and sd_s > 0.0:
                comp_s_axe[cs] = float(np.mean([
                    np.clip((d["densites_s"][cs] - mu_s) / sd_s, -3.0, 5.0) for d in da
                ]))
            else:
                comp_s_axe[cs] = 0.0

        table_axes.append({
            "code_axe": k,
            "nom_axe": NOMS_AXES[k],
            "eligible": est_elig,
            "n_amont_le_2024": v_k,
            "n_aval_2025_2026": v_aval_k,
            "X_densite_tension_amont": x_k,
            "Y_taux_percees_aval": y_taux_k,
            "Y_taux_percees_amont": y_taux_amont_k,
            "anciennete_moyenne_amont": age_k,
            "delta_R_projete": delta_r_k,
            "composantes_tension_amont": comp_s_axe,
        })

    if k_elig < 2:
        return {
            "verdict_primaire": "NON CONCLUANT",
            "motif_verdict": f"Nombre de sous-domaines éligibles insuffisant (K_elig = {k_elig} < 10).",
            "k_elig": k_elig,
            "table_axes": table_axes,
        }

    lignes_elig = [r for r in table_axes if r["eligible"]]
    vec_x = np.array([r["X_densite_tension_amont"] for r in lignes_elig], dtype=float)
    vec_y = np.array([r["Y_taux_percees_aval"] for r in lignes_elig], dtype=float)
    vec_v = np.array([r["n_amont_le_2024"] for r in lignes_elig], dtype=float)
    vec_age = np.array([r["anciennete_moyenne_amont"] for r in lignes_elig], dtype=float)
    vec_y_amont = np.array([r["Y_taux_percees_amont"] for r in lignes_elig], dtype=float)
    vec_delta_r = np.array([r["delta_R_projete"] for r in lignes_elig], dtype=float)

    vec_z, med_y, mode_bin_y = binariser_mediane_avec_repli(vec_y)
    ind_x, med_x, mode_bin_x = binariser_mediane_avec_repli(vec_x)
    for idx_r, r in enumerate(lignes_elig):
        r["Z_cible_binaire"] = int(vec_z[idx_r])
        r["I_X_mediane"] = int(ind_x[idx_r])

    variance_degeneree = (mode_bin_y == "constant_degenere") or (mode_bin_x == "constant_degenere")

    # Garde n° 5 : témoin nul « doit mourir » (flux 3)
    temoin_nul = (
        verifier_temoin_nul_doit_mourir(vec_x, vec_y, flux_rng[3])
        if executer_gardes_4_et_5
        else {"applicable": 0.0}
    )

    if variance_degeneree:
        return {
            "verdict_primaire": "NON CONCLUANT",
            "motif_verdict": "Variance nulle de X ou de Y_taux sur les sous-domaines éligibles.",
            "k_elig": k_elig,
            "table_axes": table_axes,
            "temoin_nul": temoin_nul,
        }

    # Statistiques primaires (flux 0 et flux 1)
    rho_s, p_perm = p_permutation_spearman(vec_x, vec_y, flux_rng[0], n_perm=10_000)
    auc_x = aire_sous_courbe_exacte(vec_x, vec_z)
    auc_v = aire_sous_courbe_exacte(vec_v, vec_z)
    auc_age = aire_sous_courbe_exacte(vec_age, vec_z)
    delta_a_vol = auc_x - auc_v
    delta_a_age = auc_x - auc_age
    ic_auc = intervalle_auc_reechantillonnage(vec_x, vec_z, flux_rng[1], n_rep=10_000)

    # Enrichissement à la médiane et test exact de Fisher descriptif
    moy_z = float(np.mean(vec_z))
    moy_z_haut = float(np.mean(vec_z[ind_x == 1])) if np.any(ind_x == 1) else 0.0
    e_50 = float(moy_z_haut / moy_z) if moy_z > 0 else 0.0

    a_tab = int(np.sum((ind_x == 1) & (vec_z == 1)))
    b_tab = int(np.sum((ind_x == 1) & (vec_z == 0)))
    c_tab = int(np.sum((ind_x == 0) & (vec_z == 1)))
    d_tab = int(np.sum((ind_x == 0) & (vec_z == 0)))
    or_haldane = float(((a_tab + 0.5) * (d_tab + 0.5)) / ((b_tab + 0.5) * (c_tab + 0.5)))
    _, p_fisher = stats.fisher_exact([[a_tab, b_tab], [c_tab, d_tab]], alternative="greater")

    # Corrélations partielles des rangs
    rho_part_v = spearman_partiel_exact(vec_x, vec_y, vec_v)
    rho_part_v_age = spearman_partiel_exact(vec_x, vec_y, np.column_stack([vec_v, vec_age]))
    rho_part_ancova = spearman_partiel_exact(
        vec_x, vec_y, np.column_stack([vec_y_amont, vec_v, vec_age])
    )
    rho_delta_r = spearman_exact(vec_x, vec_delta_r)

    # Règle de décision primaire gelée (section Critères de lecture gelés)
    if k_elig < 10:
        verdict = "NON CONCLUANT"
        motif_verdict = f"Effectif d'axes éligibles K_elig = {k_elig} < 10."
    elif (
        auc_x >= 0.65
        and rho_s >= 0.35
        and e_50 >= 1.35
        and p_perm <= 0.05
        and delta_a_vol >= 0.05
        and delta_a_age >= 0.00
        and rho_part_v >= 0.25
        and rho_part_v_age >= 0.20
    ):
        verdict = "CONFIRMÉ"
        motif_verdict = (
            "Tous les critères préenregistrés (amplitude, significativité par permutation, "
            "supériorité sur le volume pur et sur l'ancienneté moyenne) sont franchis simultanément."
        )
    elif (
        auc_x <= 0.52
        or rho_s <= 0.05
        or e_50 <= 1.00
        or (delta_a_vol <= 0.00 and rho_part_v <= 0.05)
    ):
        verdict = "RÉFUTÉ"
        motif_verdict = (
            "Au moins un critère de réfutation franche est atteint sur l'épreuve primaire "
            "(signal nul/inversé ou dominé par la base de volume pur)."
        )
    else:
        verdict = "NON CONCLUANT"
        motif_verdict = (
            "Signal dans la zone intermédiaire (certains seuils d'effet franchis sans réunion "
            "simultanée de tous les seuils de confirmation ni de réfutation)."
        )

    # Analyse secondaire (d) : composantes S1..S5 isolées
    comp_individuelles: list[dict[str, Any]] = []
    p_brutes_comp: list[float] = []
    for cs in cles_s:
        vec_cs = np.array([r["composantes_tension_amont"][cs] for r in lignes_elig], dtype=float)
        rho_c, p_c = p_permutation_spearman(vec_cs, vec_y, flux_rng[0], n_perm=10_000)
        auc_c = aire_sous_courbe_exacte(vec_cs, vec_z)
        p_brutes_comp.append(p_c)
        comp_individuelles.append({
            "composante": cs,
            "spearman_rho": rho_c,
            "aire_sous_courbe": auc_c,
            "p_permutation_brute": p_c,
        })
    q_bh = ajuster_benjamini_hochberg(p_brutes_comp)
    for item_c, qv in zip(comp_individuelles, q_bh):
        item_c["q_benjamini_hochberg"] = qv

    # Analyse secondaire (e) : paires de sous-domaines et procédure QAP partielle de Mantel (flux 2)
    res_dyadique = evaluer_paires_mantel(
        axes_eligibles, vec_x, vec_v, par_axe_amont, par_axe_aval, percee_aval, flux_rng[2]
    )

    # Analyse secondaire (f) : permutation au niveau des articles aval (flux 4)
    p_perm_articles_aval = permutation_articles_aval(
        elig_aval, axes_eligibles, axes_du_doc, percee_aval, vec_x, rho_s, flux_rng[4], n_perm=10_000
    )

    # Audit de symétrie R4 : omission unitaire d'un sous-domaine à la fois et concentration lexicale
    omission_unitaire: list[dict[str, Any]] = []
    for idx_omit in range(k_elig):
        masque = np.ones(k_elig, dtype=bool)
        masque[idx_omit] = False
        x_sub = vec_x[masque]
        y_sub = vec_y[masque]
        z_sub, _, m_sub = binariser_mediane_avec_repli(y_sub)
        auc_sub = aire_sous_courbe_exacte(x_sub, z_sub) if m_sub != "constant_degenere" else None
        omission_unitaire.append({
            "axe_omis": lignes_elig[idx_omit]["code_axe"],
            "spearman_rho_sans_axe": spearman_exact(x_sub, y_sub),
            "aire_sous_courbe_sans_axe": auc_sub,
        })

    comptages_globaux_s: dict[str, int] = {}
    for d in elig_amont:
        for kt, vt in d["details_termes_s"].items():
            comptages_globaux_s[kt] = comptages_globaux_s.get(kt, 0) + vt
    tot_termes_s = sum(comptages_globaux_s.values())
    part_max_terme_s = (
        max(comptages_globaux_s.values()) / float(tot_termes_s)
        if tot_termes_s > 0 else 0.0
    )
    terme_dominant_s = (
        max(comptages_globaux_s.items(), key=lambda kv: kv[1])[0]
        if comptages_globaux_s else None
    )

    audit_r4_positif = (auc_x >= 0.90) or (p_perm <= 0.001)
    audit_r4_negatif = (auc_x <= 0.50) or (rho_s <= 0.00)

    return {
        "verdict_primaire": verdict,
        "motif_verdict": motif_verdict,
        "effectifs": {
            "documents_eligibles_amont_le_2024": len(elig_amont),
            "documents_eligibles_aval_2025_2026": len(elig_aval),
            "documents_rattaches_amont": nb_rattaches_amont,
            "documents_rattaches_aval": nb_rattaches_aval,
            "sous_domaines_eligibles_K": k_elig,
            "quantile_q75_R_aval": q75_aval,
            "nb_percees_aval": int(sum(percee_aval.values())),
        },
        "metriques_primaires": {
            "aire_sous_courbe_A_XZ": auc_x,
            "intervalle_confiance_95_A_XZ": ic_auc,
            "spearman_rho_XY": rho_s,
            "p_permutation_spearman": p_perm,
            "facteur_enrichissement_mediane_E50": e_50,
            "table_contingence_2x2": {"a_hautX_hautZ": a_tab, "b_hautX_basZ": b_tab, "c_basX_hautZ": c_tab, "d_basX_basZ": d_tab},
            "rapport_cotes_haldane_anscombe": or_haldane,
            "p_fisher_unilaterale_descriptive": float(p_fisher),
            "aire_sous_courbe_volume_A_VZ": auc_v,
            "delta_A_vol": delta_a_vol,
            "aire_sous_courbe_age_A_AgeZ": auc_age,
            "delta_A_age": delta_a_age,
            "spearman_partiel_controle_volume": rho_part_v,
            "spearman_partiel_controle_volume_et_age": rho_part_v_age,
            "mediane_X": med_x,
            "mode_binarisation_X": mode_bin_x,
            "mediane_Y_taux": med_y,
            "mode_binarisation_Y": mode_bin_y,
        },
        "analyses_secondaires_integrees": {
            "a_spearman_partiel_controle_base_amont_volume_age": rho_part_ancova,
            "a_spearman_X_avec_delta_R_projete": rho_delta_r,
            "d_composantes_individuelles": comp_individuelles,
            "e_regroupements_dyadiques_mantel": res_dyadique,
            "f_p_permutation_articles_aval": p_perm_articles_aval,
        },
        "audit_symetrie_r4": {
            "declenche_positif_trop_propre": audit_r4_positif,
            "declenche_negatif_ou_nul": audit_r4_negatif,
            "total_occurrences_tension_amont": tot_termes_s,
            "terme_tension_le_plus_frequent": terme_dominant_s,
            "part_maximale_un_seul_terme_tension": part_max_terme_s,
            "omission_unitaire_sous_domaines": omission_unitaire,
        },
        "parametres_normalisation": {
            "amont_S_moyenne_ecart_type": {k: list(v) for k, v in params_s_amont.items()},
            "aval_F_moyenne_ecart_type": {k: list(v) for k, v in params_f_aval.items()},
        },
        "temoin_nul_doit_mourir": temoin_nul,
        "table_axes": table_axes,
        "exemples_articles": extraire_exemples_remarquables(elig_amont, elig_aval, scores_t_amont, scores_r_aval, percee_aval),
    }


def evaluer_paires_mantel(
    axes_eligibles: list[str],
    vec_x: np.ndarray,
    vec_v: np.ndarray,
    par_axe_amont: dict[str, list[dict[str, Any]]],
    par_axe_aval: dict[str, list[dict[str, Any]]],
    percee_aval: dict[str, int],
    rng: np.random.Generator,
    n_perm: int = 10_000,
) -> dict[str, Any]:
    """Sections 7 et 8.5 : procédure d'assignation quadratique partielle sur les paires d'axes."""
    k_elig = len(axes_eligibles)
    if k_elig < 4:
        return {"applicable": False, "nb_paires": 0}

    ensembles_amont = {k: {d["cle_canonique"] for d in par_axe_amont[k]} for k in axes_eligibles}
    ensembles_aval = {k: {d["cle_canonique"] for d in par_axe_aval[k]} for k in axes_eligibles}
    ensembles_percees_aval = {
        k: {d["cle_canonique"] for d in par_axe_aval[k] if percee_aval[d["cle_canonique"]] == 1}
        for k in axes_eligibles
    }

    paires_ij: list[tuple[int, int]] = []
    x_kl_list: list[float] = []
    p_vol_list: list[float] = []
    c_amont_list: list[float] = []
    y_pont_list: list[float] = []
    z_pont_list: list[int] = []

    for i in range(k_elig):
        ki = axes_eligibles[i]
        for j in range(i + 1, k_elig):
            kj = axes_eligibles[j]
            paires_ij.append((i, j))
            x_kl = 0.5 * (vec_x[i] + vec_x[j])
            p_vol = float(vec_v[i] * vec_v[j])
            c_am = float(len(ensembles_amont[ki] & ensembles_amont[kj]))
            n_av_i = len(ensembles_aval[ki])
            n_av_j = len(ensembles_aval[kj])
            nb_perc_communes = len(ensembles_percees_aval[ki] & ensembles_percees_aval[kj])
            y_pont = float(nb_perc_communes / math.sqrt(n_av_i * n_av_j)) if (n_av_i * n_av_j > 0) else 0.0
            taux_am = float(c_am / math.sqrt(p_vol)) if p_vol > 0 else 0.0
            z_pont = int(nb_perc_communes >= 1 and y_pont > taux_am + 1e-15)

            x_kl_list.append(x_kl)
            p_vol_list.append(p_vol)
            c_amont_list.append(c_am)
            y_pont_list.append(y_pont)
            z_pont_list.append(z_pont)

    arr_x_kl = np.array(x_kl_list, dtype=float)
    arr_ln_vol = np.log(np.maximum(1.0, np.array(p_vol_list, dtype=float)))
    arr_c_am = np.array(c_amont_list, dtype=float)
    arr_y_pont = np.array(y_pont_list, dtype=float)
    arr_z_pont = np.array(z_pont_list, dtype=int)
    w_dyad = np.column_stack([arr_ln_vol, arr_c_am])

    rho_part_obs = spearman_partiel_exact(arr_x_kl, arr_y_pont, w_dyad)
    rho_brut_obs = spearman_exact(arr_x_kl, arr_y_pont)

    # Pré-résidualisation de ry_pont sur rw_dyad pour accélérer les 10 000 permutations de sommets
    ry_p = stats.rankdata(arr_y_pont, method="average")
    rw1 = stats.rankdata(arr_ln_vol, method="average")
    rw2 = stats.rankdata(arr_c_am, method="average")
    design = np.column_stack([np.ones(len(ry_p), dtype=float), rw1, rw2])
    q_mat, _ = np.linalg.qr(design)
    res_y = ry_p - q_mat @ (q_mat.T @ ry_p)
    res_y_c = res_y - np.mean(res_y)
    norm_res_y = float(np.linalg.norm(res_y_c))

    sup_mantel = 0
    if norm_res_y >= 1e-12:
        idx_i = np.array([p[0] for p in paires_ij], dtype=int)
        idx_j = np.array([p[1] for p in paires_ij], dtype=int)
        for _ in range(n_perm):
            perm = rng.permutation(k_elig)
            x_perm_sommets = vec_x[perm]
            x_kl_b = 0.5 * (x_perm_sommets[idx_i] + x_perm_sommets[idx_j])
            ru_b = stats.rankdata(x_kl_b, method="average")
            res_u_b = ru_b - q_mat @ (q_mat.T @ ru_b)
            res_u_bc = res_u_b - np.mean(res_u_b)
            norm_u_b = float(np.linalg.norm(res_u_bc))
            rho_b = 0.0 if norm_u_b < 1e-12 else float(np.dot(res_u_bc, res_y_c) / (norm_u_b * norm_res_y))
            if rho_b >= rho_part_obs - 1e-15:
                sup_mantel += 1
        p_mantel = float((1 + sup_mantel) / (n_perm + 1))
    else:
        p_mantel = 1.0

    nb_pos_z = int(np.sum(arr_z_pont))
    if 0 < nb_pos_z < len(arr_z_pont):
        auc_paires = aire_sous_courbe_exacte(arr_x_kl, arr_z_pont)
        auc_paires_vol = aire_sous_courbe_exacte(np.array(p_vol_list, dtype=float), arr_z_pont)
        delta_auc_paires = auc_paires - auc_paires_vol
    else:
        auc_paires = None
        auc_paires_vol = None
        delta_auc_paires = None

    # Top 5 paires à forte émergence de ponts formels en 2025-2026
    ordre_top = np.argsort(-arr_y_pont)[:5]
    top_paires = [
        {
            "axe_1": axes_eligibles[paires_ij[idx][0]],
            "axe_2": axes_eligibles[paires_ij[idx][1]],
            "X_conjoint_amont": float(arr_x_kl[idx]),
            "Y_pont_aval": float(arr_y_pont[idx]),
            "cooccurrence_amont": int(arr_c_am[idx]),
            "Z_pont": int(arr_z_pont[idx]),
        }
        for idx in ordre_top
    ]

    return {
        "applicable": True,
        "nb_paires": len(paires_ij),
        "nb_paires_Z_pont_positif": nb_pos_z,
        "spearman_brut_dyadique": rho_brut_obs,
        "spearman_partiel_dyadique_controle_vol_cooc": rho_part_obs,
        "p_mantel_partiel_unilaterale": p_mantel,
        "aire_sous_courbe_paires": auc_paires,
        "aire_sous_courbe_produit_volumes": auc_paires_vol,
        "delta_aire_sous_courbe_paires": delta_auc_paires,
        "top_5_paires_ponts_aval": top_paires,
    }


def permutation_articles_aval(
    elig_aval: list[dict[str, Any]],
    axes_eligibles: list[str],
    axes_du_doc_fn: Any,
    percee_aval: dict[str, int],
    vec_x: np.ndarray,
    rho_obs: float,
    rng: np.random.Generator,
    n_perm: int = 10_000,
) -> float:
    """Analyse secondaire (f) : permute les étiquettes Percee(d') sur les articles aval."""
    n_docs = len(elig_aval)
    k_elig = len(axes_eligibles)
    if n_docs == 0 or k_elig < 2:
        return 1.0

    idx_axe = {k: i for i, k in enumerate(axes_eligibles)}
    appartenance = np.zeros((k_elig, n_docs), dtype=float)
    etiquettes = np.zeros(n_docs, dtype=float)
    for j, d in enumerate(elig_aval):
        etiquettes[j] = float(percee_aval[d["cle_canonique"]])
        for k in axes_du_doc_fn(d):
            if k in idx_axe:
                appartenance[idx_axe[k], j] = 1.0

    tailles_k = np.sum(appartenance, axis=1)
    if np.any(tailles_k == 0):
        return 1.0

    rx = stats.rankdata(vec_x, method="average")
    sx = rx - np.mean(rx)
    norm_sx = float(np.linalg.norm(sx))
    if norm_sx < 1e-12:
        return 1.0

    sup = 0
    for _ in range(n_perm):
        etiq_b = etiquettes[rng.permutation(n_docs)]
        y_k_b = (appartenance @ etiq_b) / tailles_k
        ry_b = stats.rankdata(y_k_b, method="average")
        sy_b = ry_b - np.mean(ry_b)
        norm_sy = float(np.linalg.norm(sy_b))
        rho_b = 0.0 if norm_sy < 1e-12 else float(np.dot(sx, sy_b) / (norm_sx * norm_sy))
        if rho_b >= rho_obs - 1e-15:
            sup += 1
    return float((1 + sup) / (n_perm + 1))


def extraire_exemples_remarquables(
    elig_amont: list[dict[str, Any]],
    elig_aval: list[dict[str, Any]],
    scores_t_amont: dict[str, float],
    scores_r_aval: dict[str, float],
    percee_aval: dict[str, int],
) -> dict[str, Any]:
    """Extrait les 10 articles amont les plus tendus et les 10 articles aval les plus formels."""
    top_amont = sorted(elig_amont, key=lambda d: -scores_t_amont[d["cle_canonique"]])[:10]
    top_aval = sorted(elig_aval, key=lambda d: -scores_r_aval[d["cle_canonique"]])[:10]
    return {
        "top_10_foyers_tension_amont_le_2024": [
            {
                "cle_canonique": d["cle_canonique"],
                "chemin_relatif": d["chemin_relatif"],
                "sha256": d["sha256"],
                "annee": d["annee"],
                "score_T": scores_t_amont[d["cle_canonique"]],
                "axes_actifs": d["axes_actifs"],
                "densites_s": d["densites_s"],
            }
            for d in top_amont
        ],
        "top_10_reformulations_formelles_aval_2025_2026": [
            {
                "cle_canonique": d["cle_canonique"],
                "chemin_relatif": d["chemin_relatif"],
                "sha256": d["sha256"],
                "annee": d["annee"],
                "score_R": scores_r_aval[d["cle_canonique"]],
                "percee": percee_aval[d["cle_canonique"]],
                "axes_actifs": d["axes_actifs"],
                "densites_f": d["densites_f"],
            }
            for d in top_aval
        ],
    }


# ============================================================================
# Point d'entrée principal (extraction réelle et sauvegarde JSON)
# ============================================================================

def executer_pipeline_complet(
    chemin_prereg: Path,
    racine_pdf: Path,
    sortie_json: Path,
    nb_travailleurs: int = 8,
) -> dict[str, Any]:
    """Exécute bout en bout les gardes, l'extraction PDF et les évaluations préenregistrées."""
    # 1. Garde n° 1 : préenregistrement scellé
    sha_prereg = verifier_prereg_scelle(chemin_prereg, EMPREINTE_PREREG_ATTENDUE)

    # 2. Garde n° 2 : orthogonalité lexicale sur les 6 directions
    verifier_orthogonalite_lexicale()

    # 3. Inventaire et dédoublonnage canonique
    retenus, resume_inv = inventorier_et_dedoublonner_pdfs(racine_pdf)

    # 4. Extraction parallèle par pdftotext puis tri déterministe par clé canonique
    def _tache_extraction(entree: dict[str, Any]) -> tuple[dict[str, Any], bool, str]:
        ok, flux = appeler_pdftotext(Path(entree["chemin_absolu"]))
        return entree, ok, flux

    resultats_bruts_pdf: list[tuple[dict[str, Any], bool, str]] = []
    with ThreadPoolExecutor(max_workers=nb_travailleurs) as pool:
        for res in pool.map(_tache_extraction, retenus):
            resultats_bruts_pdf.append(res)

    resultats_bruts_pdf.sort(key=lambda t: t[0]["cle_canonique"])

    # Garde n° 3 : panne d'extraction PDF > 15 %
    analyseur = AnalyseurLexicalCompile()
    docs_analyses: list[dict[str, Any]] = []
    echecs_extraction: list[dict[str, Any]] = []
    revisions_post_2024_detectees: list[str] = []
    sans_millesime: list[str] = []

    for entree, ok, flux in resultats_bruts_pdf:
        if not ok:
            echecs_extraction.append({"cle": entree["cle_canonique"], "chemin": entree["chemin_relatif"], "motif": flux})
            continue
        doc = analyseur.analyser_document(entree, flux)
        if doc["w_brut"] < 250:
            echecs_extraction.append({
                "cle": entree["cle_canonique"],
                "chemin": entree["chemin_relatif"],
                "motif": f"w_brut={doc['w_brut']}<250",
            })
            continue
        if doc["annee"] is None:
            sans_millesime.append(entree["chemin_relatif"])
        if doc["revision_post_2024"] and doc["eligible_thematique_hors_filtre_rev"]:
            revisions_post_2024_detectees.append(entree["chemin_relatif"])
        docs_analyses.append(doc)

    taux_panne = len(echecs_extraction) / float(max(1, len(retenus)))
    if taux_panne > 0.15:
        raise ErreurGardeRang1(
            f"Garde n° 3 déclenchée : taux de panne ou texte < 250 mots = {taux_panne:.2%} > 15 %"
        )

    # 5. Épreuve primaire figée
    res_primaire = evaluer_protocole_sur_documents(
        docs_analyses,
        graine=GRAINE_MAITRESSE,
        inclure_revisions_post_2024=False,
        mode_assignation_exclusive=False,
        seuil_n_min_axe=3,
        executer_gardes_4_et_5=True,
    )

    # 6. Analyses secondaires (b) assignation exclusive et (c) inclusion des révisions post-2024
    res_sec_b = evaluer_protocole_sur_documents(
        docs_analyses,
        graine=GRAINE_MAITRESSE + 100,
        inclure_revisions_post_2024=False,
        mode_assignation_exclusive=True,
        seuil_n_min_axe=2,
        executer_gardes_4_et_5=False,
    )
    res_sec_c = evaluer_protocole_sur_documents(
        docs_analyses,
        graine=GRAINE_MAITRESSE + 200,
        inclure_revisions_post_2024=True,
        mode_assignation_exclusive=False,
        seuil_n_min_axe=3,
        executer_gardes_4_et_5=False,
    )

    bilan_complet = {
        "manifeste": {
            "horodatage_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "chemin_preregistrement": str(chemin_prereg),
            "empreinte_preregistrement_verifiee": sha_prereg,
            "racine_pdf": str(racine_pdf),
            "utilitaire_extraction": "/usr/bin/pdftotext (poppler 24.02.0)",
            "graine_maitresse_seedsequence": GRAINE_MAITRESSE,
            "versions": {
                "python": sys.version.split()[0],
                "numpy": np.__version__,
                "scipy": stats.__name__ and __import__("scipy").__version__,
            },
            "cout_usd": 0.0,
        },
        "inventaire_corpus": {
            **resume_inv,
            "echecs_ou_moins_250_mots_count": len(echecs_extraction),
            "taux_panne_extraction": taux_panne,
            "echecs_details": echecs_extraction,
            "documents_sans_millesime": sans_millesime,
            "revisions_post_2024_exclues_du_primaire": revisions_post_2024_detectees,
            "repartition_annees_eligibles_primaire": _compter_annees(
                [d for d in docs_analyses if d["eligible_primaire"]]
            ),
        },
        "epreuve_primaire": res_primaire,
        "variantes_secondaires": {
            "b_assignation_primaire_exclusive_nmin2": {
                "verdict_descriptif": res_sec_b.get("verdict_primaire"),
                "k_elig": res_sec_b.get("effectifs", {}).get("sous_domaines_eligibles_K", res_sec_b.get("k_elig")),
                "metriques_primaires": res_sec_b.get("metriques_primaires"),
            },
            "c_incluant_revisions_post_2024": {
                "verdict_descriptif": res_sec_c.get("verdict_primaire"),
                "k_elig": res_sec_c.get("effectifs", {}).get("sous_domaines_eligibles_K", res_sec_c.get("k_elig")),
                "metriques_primaires": res_sec_c.get("metriques_primaires"),
            },
        },
    }

    sortie_json.parent.mkdir(parents=True, exist_ok=True)
    sortie_json.write_text(json.dumps(bilan_complet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return bilan_complet


def _compter_annees(docs: list[dict[str, Any]]) -> dict[str, int]:
    compteur: dict[str, int] = {}
    for d in docs:
        a = str(d["annee"])
        compteur[a] = compteur.get(a, 0) + 1
    return dict(sorted(compteur.items()))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Extracteur rétrodictif des foyers de tension (Pas 0, Rang 1).")
    dossier_defaut = Path(
        "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
        "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/pas0-rang1-foyers-tension"
    )
    parser.add_argument(
        "--prereg",
        type=Path,
        default=dossier_defaut / "prereg-pas0-rang1-retrodiction-foyers-tension-2024-vers-2025-2026-v1.md",
    )
    parser.add_argument(
        "--racine-pdf",
        type=Path,
        default=DEPOT_RACINE / "docs" / "sources" / "pdf",
    )
    parser.add_argument(
        "--sortie-json",
        type=Path,
        default=dossier_defaut / "resultats-retrodiction-rang1-v1.json",
    )
    parser.add_argument("--travailleurs", type=int, default=8)
    args = parser.parse_args(argv)

    bilan = executer_pipeline_complet(args.prereg, args.racine_pdf, args.sortie_json, args.travailleurs)
    ep = bilan["epreuve_primaire"]
    mp = ep["metriques_primaires"]
    print(
        f"Verdict primaire : {ep['verdict_primaire']} | "
        f"K_elig={ep['effectifs']['sous_domaines_eligibles_K']} | "
        f"A(X,Z)={mp['aire_sous_courbe_A_XZ']:.4f} | "
        f"rho_S={mp['spearman_rho_XY']:+.4f} (p={mp['p_permutation_spearman']:.4f}) | "
        f"E_50%={mp['facteur_enrichissement_mediane_E50']:.3f} | "
        f"Delta_A_vol={mp['delta_A_vol']:+.4f}"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ErreurGardeRang1 as exc_garde:
        print(f"ARRÊT GARDE R5 : {exc_garde}", file=sys.stderr)
        sys.exit(1)
