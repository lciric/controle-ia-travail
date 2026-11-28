"""Vérificateur v5 fidélité : chaque renvoi de ligne des registres que cite la v5, dans la version qu'elle épingle.
Lecture seule : `git show COMMIT:chemin` (aucune écriture git) ; « vivant » = tête 9ecd952, que cite la v5. Usage : python3 -I -B renvois_depot_v5.py"""
import hashlib, subprocess, sys
R = "/home/user/controle-ia-travail"

def version(commit, chemin):
    if commit is None:
        return open(f"{R}/{chemin}", "rb").read()
    return subprocess.run(["git", "-C", R, "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout

# (empreinte citée par la v5, commit qui la porte ou None pour le fichier vivant, chemin, [(ligne, identifiant attendu)])
CAS = [
 ("38579d98", "8bd4a75", "registres/decisions.md", [(446, "N-025"), (453, "R-262"), (456, "N-028"), (457, "R-265"), (461, "R-269"), (468, "N-029"), (469, "R-276")]),
 ("94ebe409", "8bd4a75", "registres/go.md", [(32, "GO-2026-10-20-05"), (34, "GO-2026-10-20-07"), (35, "GO-2026-10-20-08")]),
 ("cc1b108d", "43cd3ac", "registres/decisions.md", [(392, "P-015"), (477, "R-283"), (447, "N-025"), (454, "R-262"), (457, "N-028"), (458, "R-265"), (462, "R-269"), (469, "N-029"), (470, "R-276")]),
 ("05e7fccd", "43cd3ac", "registres/go.md", [(33, "GO-2026-10-20-05"), (34, "GO-2026-10-20-06"), (35, "GO-2026-10-20-07"), (36, "GO-2026-10-20-08")]),
 ("e8b73c64", "9ecd952", "registres/decisions.md", [(453, "N-025"), (460, "R-262"), (463, "N-028"), (464, "R-265"), (468, "R-269"), (475, "N-029"), (476, "R-276"), (483, "R-283"), (392, "P-015"),
   (393, "P-016"), (394, "P-017"), (395, "P-018"), (396, "N-030"), (490, "R-290"), (495, "R-295"), (496, "R-296"), (497, "R-297"), (498, "R-298"), (500, "R-300"), (502, "R-302"), (503, "R-303"), (504, "R-304"), (505, "R-305"), (506, "R-306")]),
 ("1a392407", "9ecd952", "registres/go.md", [(33 + k, f"GO-2026-10-20-{5 + k:02d}") for k in range(8)]),
]
fautes = 0
for emp, commit, chemin, lignes in CAS:
    data = version(commit, chemin)
    h = hashlib.sha256(data).hexdigest()
    okv = h.startswith(emp)
    fautes += not okv
    print(f"== {chemin} @ {commit or 'vivant'} : {h[:16]}… {'= cité' if okv else 'DIFFÉRENT de ' + emp}")
    txt = data.decode("utf-8").splitlines()
    for n, ident in lignes:
        ok = txt[n - 1].startswith(f"| {ident} |")
        fautes += not ok
        print(f"  l. {n} : {ident} {'OK' if ok else 'ÉCART : ' + txt[n - 1][:30]}")
# épreuve R5 : un décalage d'une ligne doit être vu
txt = version("9ecd952", "registres/decisions.md").decode("utf-8").splitlines()
print("R5 : R-262 à la l. 459 (décalée) :", "ACCEPTÉ (faute)" if txt[458].startswith("| R-262 |") else "rejeté")
print(f"fautes : {fautes}")
sys.exit(1 if fautes else 0)
