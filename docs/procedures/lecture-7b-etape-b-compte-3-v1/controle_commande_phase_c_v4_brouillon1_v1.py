#!/usr/bin/env python3
"""Contrôles par programme du brouillon 1 de la commande phase C v4 (décision R-2980) : différentiel v3 -> v4 et filtres du bloc 1C.

1. Différentiel ligne à ligne (difflib) : plages changées, lignes ôtées et ajoutées ; blocs bash qui diffèrent.
2. Filtres : `INTERDITS_NOMS_B` et `INTERDITS_CONTENU_B`, lus dans le bloc 1C du brouillon lui-même, joués par `grep -i -E` (comme
   le bloc C5) sur le chemin de la pièce ajoutée, son compagnon et leur forme au bordereau ; cas témoins : un nom que le filtre doit
   arrêter (R5 : cas sain et artefact).
Usage, depuis la racine du dépôt :  python3 -I -B <ce fichier>   (code 0 : tout conforme ; 1 sinon)
"""
import difflib
import hashlib
import pathlib
import re
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
V3 = ICI / "commande-compte-3-phase-c-v3.md"
V4 = ICI / "commande-compte-3-phase-c-v4-brouillon1.md"
EMPREINTE_V3 = "9d7889198238c171447a06f56f1a37beb4190572c3a9ceceb18144541c258d2e"
NOMS_BLOCS = ["0b-C", "1C", "2C", "C0", "C1a", "C1", "C2", "C3", "C4a", "C4-attente", "C4b", "C5", "C6", "C7", "F-C", "M"]
BLOCS_ATTENDUS = ["0b-C", "C5", "F-C"]
R7 = "20261114-001352-t07-lecture-reel"
ko = 0


def dit(ok, texte):
    global ko
    ko += 0 if ok else 1
    print(("conforme : " if ok else "ÉCART : ") + texte)


a, b = V3.read_bytes(), V4.read_bytes()
print(f"v3 : {hashlib.sha256(a).hexdigest()} ; {len(a)} octets")
print(f"v4, brouillon 1 : {hashlib.sha256(b).hexdigest()} ; {len(b)} octets")
dit(hashlib.sha256(a).hexdigest() == EMPREINTE_V3, "empreinte de la v3 égale à l'empreinte scellée")
la, lb = a.decode("utf-8").splitlines(), b.decode("utf-8").splitlines()
print(f"lignes : v3 {len(la)}, v4 {len(lb)}")
print("\n== 1. Différentiel ==")
otees = ajoutees = plages = 0
for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, la, lb, autojunk=False).get_opcodes():
    if op == "equal":
        continue
    plages += 1
    otees += i2 - i1
    ajoutees += j2 - j1
    print(f"-- plage {plages} ({op}) : v3 l. {i1 + 1}-{i2} -> v4 l. {j1 + 1}-{j2}")
    for x in la[i1:i2]:
        print("  - " + x)
    for x in lb[j1:j2]:
        print("  + " + x)
print(f"bilan : {plages} plages ; {otees} lignes ôtées ; {ajoutees} lignes ajoutées ; {len(la) - otees} lignes de la v3 gardées à l'octet")
dit(plages == 9, "neuf plages changées, une par couple du programme de couples")
ba, bb = (re.findall(r"```bash\n(.*?)```", x.decode("utf-8"), re.S) for x in (a, b))
dit(len(ba) == len(bb) == 16, "seize blocs bash dans les deux versions")
diff = [NOMS_BLOCS[i] for i, (x, y) in enumerate(zip(ba, bb)) if x != y]
print("blocs bash qui diffèrent :", ", ".join(diff))
dit(diff == BLOCS_ATTENDUS, "seuls les blocs 0b-C (nom du fichier), C5 (pièce et commentaire) et F-C (numéro de version au journal) diffèrent")
for nom in ("bac-etape-b-compte-3-v2", "variables-v2.sh", "appel-etape-b-lance-v2.txt", "bordereau-remise-v2.txt", "verdict/t07-etape-b-compte-3-v1",
            "commande-compte-3-phase-a-v2.md", "<<"):
    dit(a.decode().count(nom) == b.decode().count(nom), f"« {nom} » : même nombre d'occurrences ({b.decode().count(nom)})")
dit("phase-c-v4-brouillon" not in b.decode(), "le nom de brouillon ne figure nulle part dans la commande")

print("\n== 2. Filtres du bloc 1C sur la pièce ajoutée ==")
t = b.decode("utf-8")
motifs = {k: re.search(rf"^{k}='([^'\n]*)'$", t, re.M).group(1) for k in ("INTERDITS_NOMS_B", "INTERDITS_CONTENU_B")}
chemin = f"diag/{R7}/sondes-t07.json"
cas = [chemin, chemin + ".sha256", f"{'0' * 64}  ./{chemin}"[66:], f"{'0' * 64}  ./{chemin}.sha256"[66:]]
for k, m in motifs.items():
    print(f"{k} = {m}")
    dit(re.search(rf"^{k}='{re.escape(m)}'$", a.decode("utf-8"), re.M) is not None, f"{k} égal à celui de la v3")
    for c in cas:
        n = subprocess.run(["grep", "-c", "-i", "-E", m], input=c + "\n", capture_output=True, text=True, env={"LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin"}).stdout.strip()
        dit(n == "0", f"{k} ne touche pas « {c} » ({n} ligne)")
for k, temoin in (("INTERDITS_NOMS_B", f"./diag/{R7}/lecture-sondes-t06.json"), ("INTERDITS_NOMS_B", "./donnees/x/sondes-neuves-t07.npz"),
                  ("INTERDITS_CONTENU_B", "plan de l'étape B bis")):
    n = subprocess.run(["grep", "-c", "-i", "-E", motifs[k]], input=temoin + "\n", capture_output=True, text=True, env={"LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin"}).stdout.strip()
    dit(n == "1", f"témoin : {k} arrête bien « {temoin} » ({n} ligne)")
print(f"\nBILAN : {'TOUT CONFORME' if ko == 0 else f'{ko} ÉCART(S)'}")
sys.exit(0 if ko == 0 else 1)
