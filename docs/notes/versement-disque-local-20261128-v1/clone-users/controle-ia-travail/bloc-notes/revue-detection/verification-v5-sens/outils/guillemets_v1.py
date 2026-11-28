"""Phrases anglaises du rapport v5-sens cherchées sur leur page (espaces normalisés), plus un artefact (R5)."""
import re
import sys

base = sys.argv[1]


def n(p):
    return re.sub(r"\s+", " ", open(p, encoding="utf-8").read())


cas = [
    ("verification-v5-sens/pages/AP/r018.txt", "activates somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive responses from control responses", True),
    ("verification-v5-sens/pages/BX/p006.txt", "we examine probes’ ability to distinguish transcripts containing normal conversational data from those exhibiting the studied behavior. For that we measure the recall at fixed 1% FPR threshold", True),
    ("verification-v5-sens/pages/BX/p006.txt", "Sandbagging 1.00 0.04 0.03", True),
    ("txt-nouveaux/2606.12618v2/p07.txt", "asking a Gender Secret model whether it knows the user’s age or hair colour", True),
    ("txt-nouveaux/2606.12618v2/p11.txt", "DYL, by contrast, retains strong performance on the prompted variants", True),
    ("verification-v5-sens/pages/AP/r018.txt", "activates somewhat when deception is incentivized (rather than performed) which still allows the probe to distinguish deceptive responses from Alpaca responses", False),
    ("verification-v5-sens/pages/BX/p006.txt", "Sandbagging 1.00 0.04 0.30", False),
]
mauvais = 0
for chemin, phrase, attendu in cas:
    trouve = phrase in n(base + "/" + chemin)
    ok = trouve == attendu
    mauvais += not ok
    print(("OK" if ok else "ECHEC"), "trouvé" if trouve else "absent", "| attendu", "trouvé" if attendu else "absent (artefact)", "|", chemin, "|", phrase[:60])
print("echecs", mauvais)
sys.exit(1 if mauvais else 0)
