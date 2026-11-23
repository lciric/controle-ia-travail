import re
M = re.compile(r"(?<![\w-])lignes?\s+(\S+)", re.I)
def regle(p):
    n = " ".join(p.split()).lower()
    if re.search(r"(?<![\w-])bras a(?![\w-])", n) is None: return False
    if re.search(r"(?<![\w-])ligne 1(?![\w-]|[.,]\d)", n) is None: return False
    for m in M.finditer(n):
        if m.group(0).split()[0] != "ligne" or m.group(1).rstrip(".,;:)") != "1": return False
    if re.search(r"moniteur|seconde|bras b|bras c", n): return False
    return True
real = "Même mot (GO-2026-11-22-147) : bras A, ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes), devis docs/notes/relance-organismes-discrets-v1/devis-bras-a-v5.md (40b999f8…), plafond 18 USD ; départ seulement après les préalables de 13.2 tenus, texte v2 scellé, lanceur prêt et contre-lu, et crédit suffisant."
sains = [real, "ligne 1 du bras A", "Ligne  1 du Bras A (devis v5, carte)", "lecture : ligne 1 du bras A ; plafond 18 USD"]
ref = ["ligne 2 du bras A","ligne 10 du bras A","ligne 1 du bras B","lignes 1 et 2 du bras A","ligne 1 du bras A et ligne 2 du bras A",
 "ligne 1.5 du bras A","seconde ligne du bras A","course du bras A","ligne 1 du bras AB",
 real.replace("ligne 1 de carte","ligne 2 de carte"), real.replace("ligne 1 de carte","lignes 1 et 2 de carte"),
 real.replace("ligne 1 de carte (fabrication et rejeu honnête, 128 épisodes)","moniteurs"), real.replace("bras A","bras B"),
 real+" ligne 2", real.replace("ligne 1 de carte","ligne 1 et ligne 2 de carte")]
print([regle(x) for x in sains]); print([regle(x) for x in ref])
