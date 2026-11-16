# Écrit le 2026-11-16T12:12:39Z (date -u) par le préparateur des préalables de la phase C v3 (sous-agent de la session mère, modèle A).
# Bibliothèque standard seule ; lit l'entrée standard ; n'écrit rien. Usage : git show refs/remotes/origin/main:registres/scellements-v1.md | python3 -I -B ordre_prealables_rv1_v1.py
"""Contrôle d'ordre des préalables (R-V1), lecture seule, sur un registre de scellements lu sur l'entrée standard.

Ordre tenu : CODE-MOTS-ET-COUT-T06 < AUDIT-FUITES-T07 < LECTURE-T08-BASE-A <= ISSUE-MOTS-ET-COUT-T06 (dates
AAAA-MM-JJTHH:MM:SSZ, comparables comme chaînes). Chaque clé doit avoir exactement une ligne. N'imprime que les clés et
leurs dates. Codes : 0 ordre tenu ; 2 clé absente, en double ou ordre non tenu.
"""
import re
import sys

ORDRE = ("CODE-MOTS-ET-COUT-T06", "AUDIT-FUITES-T07", "LECTURE-T08-BASE-A", "ISSUE-MOTS-ET-COUT-T06")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z")
vues = {k: [] for k in ORDRE}
for ligne in sys.stdin:
    c = [x.strip() for x in ligne.strip().strip("|").split("|")]
    if len(c) == 4 and c[0] in vues:
        vues[c[0]].append(c[1])
for k in ORDRE:
    if len(vues[k]) != 1 or not DATE.fullmatch(vues[k][0]):
        print(f"ORDRE R-V1 : ARRÊT — {k} : {len(vues[k])} ligne(s) au format attendu")
        sys.exit(2)
t = [vues[k][0] for k in ORDRE]
print(" ; ".join(f"{k} {d}" for k, d in zip(ORDRE, t)))
ok = t[0] < t[1] < t[2] <= t[3]
print("ORDRE R-V1 : " + ("tenu" if ok else "NON TENU"))
sys.exit(0 if ok else 2)
