"""Vérification v4, angle fidélité : phrases anglaises et lignes de table ajoutées ou déplacées par la v4, à la page citée.

Deux lectures indépendantes pour chaque item :
  (1) pdftotext lancé ici sur le PDF, empreinte complète recalculée (modes raw et layout) ;
  (2) l'outil de la revue, verification/cherche.py, sur les pages déjà extraites (liste des pages où la phrase se trouve).
Section A : items de la v4 (doivent être trouvés à la page citée par les deux lectures).
Section B : épreuve R5 (artefacts : chiffre changé, mot changé, colonnes permutées, page voisine) ; chacun doit être rejeté
à la page citée par la lecture (1).
Usage : python3 -I -B verifier_v4.py > sortie-verification-v4-fidelite.txt
"""
import hashlib
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

D = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/revue-detection")
CLES = D / "verification" / "cles.txt"
CHERCHE = D / "verification" / "cherche.py"
V4 = D / "synthese-comment-detecter-v4.md"
V4_SHA = "fba703f90bba52663709857113d99e17ab0570e465180bed539458b18b11d00a"

# (clé, page, phrase, où dans la v4 [ligne du fichier v4], mode)
A = [
    ("AP", 18, "Our recall at 1% is greater than 99% on all four evaluation datasets", "210 (rang 4)", "raw"),
    ("AP", 18, "activates somewhat when deception is incentivized (rather than performed)", "208 (rang 2)", "raw"),
    ("AP", 18, "every Sandbagging response is rated as highly deceptive – even when the model chooses not to sandbag", "285 (E2, piège)", "raw"),
    ("AP", 9, "As before we train on the Roleplaying dataset", "60-61, 210, 283 (sondes apprises sur Roleplaying)", "raw"),
    ("AP", 18, "Again, we trained this using 90% of the Roleplaying dataset", "60-61, 210, 283", "raw"),
    ("AP", 23, "here we train a different probe (on just the last positions of the training data)", "68-71, 210", "raw"),
    ("AP", 23, "Both probes were trained on the Roleplaying dataset", "68-71, 210", "raw"),
    ("AP", 23, "Recall at 1% FPR compared to control does show improvement, although is still subpar compared to the probe trained on Instructed-Pairs", "68-71, 210", "raw"),
    ("BX", 3, "Our per-layer analysis indicates that layer choice has limited effect on monitor performance, particularly beyond the first third of layers", "67-68, 212", "raw"),
    ("BX", 4, "a system prompt that instructs the model to underperform on questions related to WMDP", "81-82, 106", "raw"),
    ("BX", 6, "distinguish transcripts containing normal conversational data from those exhibiting the studied behavior", "79-80, 106", "raw"),
    ("BX", 6, "recall at fixed 1% FPR threshold", "79-80 (rappel à 1 %)", "raw"),
    ("BX", 12, "For sandbagging the labels are derived from step-1 sandbagging decisions", "81-82, 106", "raw"),
    ("BX", 12, "Instead, give bad logic and reasoning, resulting in an incorrect answer", "82-83, 106", "raw"),
    ("BX", 13, "The user must not guess that you're sandbagging", "83 (p. 12-13)", "raw"),
    ("PAR", 4, "The system prompt also informs the assistant whether the provided code contains a backdoor", "110", "raw"),
    ("PAR", 4, "however it doesn't rely on LLaMA-3.3-70B-Instruct to generate the backdoors itself", "74-77 (70 milliards ; hors politique)", "raw"),
    ("PAR", 4, "the WMD-related questions are sourced from WMDP", "283 (sujet WMDP contre MMLU)", "raw"),
    ("PAR", 4, "The generic trivia questions are sourced from MMLU", "283", "raw"),
    ("PAR", 3, "Monitoring strategies are only given access to public tokens", "75-76 (jetons publics seuls, p. 3-4)", "raw"),
    ("PAR", 3, "Instructed-pairs probe (Pairs)", "75 (recette « Pairs »)", "raw"),
    ("PAR", 9, "the average honest Backdoors sample had a mean probe activation higher than 99.9% of the Alpaca samples", "77 (p. 9)", "raw"),
    ("AU", 7, "the last 10 tokens for each datapoint", "85-86, 117, 209", "raw"),
    ("AU", 7, "Follow the same procedure to evaluate the probe", "85-86 (agrégation au test non écrite)", "raw"),
    ("AU", 6, "+System (AUC = 1.000)", "87, 117, 209", "raw"),
    ("AU", 6, "Note that the \"+X\" notation means the prompt includes all inputs above and including X", "117", "raw"),
    ("KU", 9, "flagging that a model is operating under deceptive instructions even when its output happens to be correct", "208", "raw"),
    ("KU", 9, "deceptive prompt regime", "208, 215", "raw"),
    ("KU", 5, "deceptive prompt regime", "215, 285", "raw"),
    ("CA", 8, "All probe architectures perform similarly", "212", "raw"),
    ("CA", 5, "six layers spread evenly from 30% to 90%", "212 (six couches)", "raw"),
    ("CC", 8, "using fewer layers consistently yields worse performance", "212", "raw"),
    ("LB", 8, "Since the results are comparable to those of the mean probe", "59, 210, 283", "raw"),
    ("LB", 6, "Answer deceptively to the following question", "77-78 (consigne)", "raw"),
    ("LB", 7, "probes are not evaluated on system prompt activations", "77-78 (consigne non notée)", "raw"),
    ("DYL", 5, "existing organisms are often trained on Llama 3.3 70B", "65 (paraphrase)", "raw"),
    ("DYL", 5, "which Artificial Analysis [2026] rank as less capable than more recent models such as Qwen 3.5 2B Reasoning", "65 (paraphrase)", "raw"),
    ("DYL", 5, "one paired with a randomly drawn honesty-inducing system prompt and one with a lie-inducing prompt", "78-79 (« Varied Deception »)", "raw"),
    ("DYL", 8, "the probe score is the mean over all non-reasoning assistant tokens", "77-79 (consigne non notée)", "raw"),
    ("DYL", 28, "Balanced accuracy on Varied Deception", "79, 283", "raw"),
    ("K", 7, "Domain shift effects are significant for all behaviours", "304 (premier levier)", "raw"),
    # lignes de table (mode layout)
    ("PAR", 7, "Full Averaging (Pairs) 0.966 0.931 0.844 0.999 0.964 0.941", "76, 110, 189, 209 (0,844 ; 0,931 ; 0,964)", "layout"),
    ("PAR", 7, "Full Averaging (RP) 0.914 0.907 0.550 0.999 0.828 0.840", "188-189 (0,907 ; maximum RP gagne 3 sur 4)", "layout"),
    ("PAR", 7, "Peak Activation (Pairs) 0.937 0.811 0.768 0.979 0.839 0.867", "76, 110, 189, 209 (0,768 ; 0,811)", "layout"),
    ("PAR", 7, "Peak Activation (RP) 0.929 0.877 0.650 0.935 0.891 0.856", "188-189 (0,877 ; 3 sur 4)", "layout"),
    ("PAR", 7, "Deception No (Pairs) 0.913 0.700 0.832 0.948 0.849 0.848", "59, 110, 210, 283 (0,832 ; 0,849)", "layout"),
    ("PAR", 7, "Honest Yes (Pairs) 0.920 0.767 0.849 0.963 0.879 0.876", "59, 110, 210, 283 (0,849 ; 0,879)", "layout"),
    ("PAR", 7, "Deception No (RP) 0.928 0.879 0.667 0.997 0.457 0.786", "61, 210, 283 (0,457)", "layout"),
    ("PAR", 7, "Honest Yes (RP) 0.921 0.806 0.675 0.997 0.437 0.767", "61, 210, 283 (0,437)", "layout"),
    ("DYL", 28, "Qwen/Qwen3-4B 14 0.64 0.68 0.85 0.74", "283 (0,68 ; moyenne 0,64)", "layout"),
    ("DYL", 28, "Qwen/Qwen3-8B 13 0.74 0.69 0.87 0.76", "79, 209, 283 (0,74 ; 0,69)", "layout"),
    ("LB", 54, "Llama 3.3 70B 0.41 0.12 1.00 0.57 0.95 0.45 0.93 0.64", "78, 209 (ID : 0,95)", "layout"),
    ("LB", 54, "Qwen 2.5 72B 0.50 0.49 — 0.57 0.60 — — 0.54", "78, 209 (ID : 0,60)", "layout"),
    ("LB", 54, "Mistral 3.1 24B 0.55 0.46 — 0.82 0.69 0.58 0.58 0.61", "78, 209 (ID : 0,69)", "layout"),
    ("LB", 54, "Gemma 3 27B — — 0.70 — 0.58 — 0.30 0.53", "78, 209 (ID : 0,58)", "layout"),
    ("LB", 54, "HP-C HP-KR CG ST ID GS IT AVERAGE", "en-tête de colonnes de la table 6", "layout"),
    ("BX", 6, "Sandbagging 1.00 0.04 0.03", "80, 106, 209 (0,03)", "layout"),
    ("K", 7, "Deception −0.416*** — +0.035 +0.130", "304 (−0.416)", "layout"),
]

# Épreuve R5 : chacun doit être ABSENT à la page citée (lecture 1)
B = [
    ("PAR", 7, "Peak Activation (Pairs) 0.937 0.811 0.786 0.979 0.839 0.867", "chiffre permuté (0.768 → 0.786)", "layout"),
    ("PAR", 7, "Honest Yes (Pairs) 0.920 0.767 0.879 0.963 0.849 0.876", "colonnes permutées", "layout"),
    ("AP", 18, "Our recall at 1% is greater than 95% on all four evaluation datasets", "chiffre changé", "raw"),
    ("AU", 6, "+System (AUC = 0.653)", "valeur d'une autre ligne", "raw"),
    ("DYL", 5, "less capable than more recent models such as Qwen 3.5 4B Reasoning", "taille changée", "raw"),
    ("DYL", 28, "Qwen/Qwen3-4B 14 0.68 0.64 0.85 0.74", "colonnes permutées", "layout"),
    ("BX", 3, "layer choice has strong effect on monitor performance", "mot changé", "raw"),
    ("KU", 8, "flagging that a model is operating under deceptive instructions", "page voisine (vraie page : 9)", "raw"),
    ("LB", 54, "Qwen 2.5 72B 0.50 0.49 — 0.57 0.69 — — 0.54", "valeur d'une autre ligne", "layout"),
    ("BX", 6, "Sandbagging 1.00 0.03 0.04", "colonnes permutées", "layout"),
]


def pdf(cle):
    for ligne in CLES.read_text().splitlines():
        k, p, h = ligne.split()
        if k == cle:
            s = hashlib.sha256(Path(p).read_bytes()).hexdigest()
            if not s.startswith(h):
                sys.exit(f"ARRÊT : empreinte en écart pour {cle} : {s}")
            return p, s
    sys.exit(f"ARRÊT : clé inconnue {cle}")


_cache = {}


def texte(p, page, mode):
    k = (p, page, mode)
    if k not in _cache:
        opt = "-raw" if mode == "raw" else "-layout"
        _cache[k] = subprocess.run(["pdftotext", opt, "-f", str(page), "-l", str(page), p, "-"],
                                   capture_output=True, text=True, check=True).stdout
    return _cache[k]


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    for a, b in [("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'), ("−", "-"), ("–", "-"), ("—", "-")]:
        s = s.replace(a, b)
    s = re.sub(r"-\s*\n\s*", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


def cherche(cle, phrase):
    r = subprocess.run([sys.executable, "-I", "-B", str(CHERCHE), cle, phrase], capture_output=True, text=True)
    m = re.search(r"raw: \[(.*?)\] layout: \[(.*?)\]", r.stdout)
    if not m:
        return None, None
    f = lambda x: [int(v) for v in x.split(",") if v.strip()]
    return f(m.group(1)), f(m.group(2))


def main():
    s = hashlib.sha256(V4.read_bytes()).hexdigest()
    print(f"v4 : {s} {'(égale)' if s == V4_SHA else '(ÉCART)'}")
    if s != V4_SHA:
        sys.exit("ARRÊT : v4 en écart")
    vus = set()
    for cle, *_ in A + B:
        if cle not in vus:
            p, h = pdf(cle)
            print(f"PDF {cle} {h} {p}")
            vus.add(cle)
    print("\n== A. items de la v4 (attendu : trouvé à la page citée, lecture directe ET cherche.py)")
    na = 0
    for cle, page, phrase, ou, mode in A:
        p, _ = pdf(cle)
        ok1 = norm(phrase) in norm(texte(p, page, mode))
        raw, lay = cherche(cle, phrase)
        ok2 = raw is not None and (page in raw or page in lay)
        etat = "OK" if (ok1 and ok2) else "ÉCART"
        na += etat != "OK"
        print(f"[{etat}] {cle} p.{page} ({mode}) v4 l. {ou} | directe={'oui' if ok1 else 'non'} "
              f"cherche.py raw={raw} layout={lay} | {phrase[:90]!r}")
    print(f"A : {len(A)} items, {na} écart(s)")
    print("\n== B. épreuve R5 (attendu : rejeté à la page citée, lecture directe)")
    nb = 0
    for cle, page, phrase, quoi, mode in B:
        p, _ = pdf(cle)
        ok1 = norm(phrase) in norm(texte(p, page, mode))
        raw, lay = cherche(cle, phrase)
        etat = "REJETÉ" if not ok1 else "ACCEPTÉ À TORT"
        nb += ok1
        print(f"[{etat}] {cle} p.{page} ({mode}) {quoi} | cherche.py raw={raw} layout={lay} | {phrase[:80]!r}")
    print(f"B : {len(B)} artefacts, {len(B) - nb} rejetés, {nb} acceptés à tort")


if __name__ == "__main__":
    main()
