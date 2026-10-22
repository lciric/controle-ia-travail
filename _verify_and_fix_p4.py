import os
import json
import hashlib

d = "bloc-notes/p4-instrument/chaine-v4"

# 1. controles_avant_depense_p4_v1.sh
f_ctrl = os.path.join(d, "controles_avant_depense_p4_v1.sh")
with open(f_ctrl, "r", encoding="utf-8") as f:
    content = f.read()

assert "$DEPOT" not in content.split("# 12. garde de calcul")[1], "Assertion Failed: $DEPOT is still in bloc 12 of controles_avant_depense_p4_v1.sh"
assert "eg=$(sha256sum .claude/hooks/garde_calcul.py 2>/dev/null | cut -d' ' -f1)" in content, "Assertion Failed: eg assignment missing or incorrect in controles_avant_depense_p4_v1.sh"
assert '[ "$eg" = "579f65c8ae3002d8e5c61698d636549b0401da3acff6bce718ae88e93664a6f2" ] && ok "empreinte de la garde gelée avant exécution" || ko "empreinte de la garde gelée avant exécution ($eg)"' in content, "Assertion Failed: ok/ko logic missing or incorrect in controles_avant_depense_p4_v1.sh"

# 2. recuperation_p4_v1.sh
f_recup = os.path.join(d, "recuperation_p4_v1.sh")
with open(f_recup, "r", encoding="utf-8") as f:
    content = f.read()

assert '"$D/arret.txt"' not in content, "Assertion Failed: $D/arret.txt still found in recuperation_p4_v1.sh"
assert '"$T/arret.txt"' in content, "Assertion Failed: $T/arret.txt not found in recuperation_p4_v1.sh"

# 3. repetition_jouet_p4_v1.sh
f_rep = os.path.join(d, "repetition_jouet_p4_v1.sh")
with open(f_rep, "r", encoding="utf-8") as f:
    content = f.read()

assert '"$R/instance-delai.sh"' in content, "Assertion Failed: instance-delai.sh not found in repetition_jouet_p4_v1.sh"

# 4. JSON Paires Test
f_json = os.path.join(d, "paires-candidat2-chaine-v4-v1.json")
f_brouillon = "bloc-notes/p4-instrument/P4-instrument-v1-brouillon4.md"

assert os.path.exists(f_brouillon), f"Assertion Failed: {f_brouillon} does not exist"

with open(f_brouillon, "r", encoding="utf-8") as f:
    b4_content = f.read()

with open(f_json, "r", encoding="utf-8") as f:
    pairs = json.load(f)

for p in pairs:
    ancien = p["ancien"]
    count = b4_content.count(ancien)
    assert count == 1, f"Assertion Failed: Expected exactly 1 occurrence of '{ancien[:50]}...', found {count}"

# 5. SHA256 Recalculation
for f in os.listdir(d):
    fp = os.path.join(d, f)
    if os.path.isfile(fp) and not f.endswith(".sha256"):
        with open(fp, "rb") as file:
            h = hashlib.sha256(file.read()).hexdigest()
        with open(fp + ".sha256", "w", encoding="utf-8", newline="\n") as sha_file:
            sha_file.write(f"{h}  {f}\n")

# Cleanup scripts
cleanup_list = ["_fix_p4.py", "_do_porte_a.py", "_verify_and_fix_p4.py"]
for f in cleanup_list:
    if os.path.exists(f):
        os.remove(f)

print("Porte A Validated Successfully with Assertions.")
