"""Remplissage des deux lignes du brouillon 14 (procédure du rapport contre-lecture-brouillon14-v1.md, points 1 à 6)."""
import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "src")
from controle_ia import prereg  # noqa: E402

BROUILLON = Path("brouillons/barreau8-lecture-sondes-v1/prereg-lecture-sondes-barreau8-v1-brouillon14.md")
RAPPORT = Path("brouillons/barreau8-lecture-sondes-v1/contre-lecture-brouillon14-v1.md")
CIBLE = Path("prereg/lecture-sondes-barreau8-v1.md")
SHA_BROUILLON = "5b503e28e6b81285a792575f878642bbd529888cc886e7cd4ddcf80257e39891"
SHA_RAPPORT = "d7d688f7bf5c5c39dae902f886bb9c4c8417697f563d8e60cc23a495d8f4341e"
MARQUEUR_F3 = "À REMPLIR — À FIXER : tirée par la session mère au scellement"

entropie = sys.argv[1]
assert entropie.isdigit() and str(int(entropie)) == entropie
art = Path(sys.argv[2])  # dossier des artefacts d'essai de la garde
b = BROUILLON.read_bytes()
assert hashlib.sha256(b).hexdigest() == SHA_BROUILLON
assert hashlib.sha256(RAPPORT.read_bytes()).hexdigest() == SHA_RAPPORT
assert RAPPORT.with_name(RAPPORT.name + ".sha256").read_text().split()[0] == SHA_RAPPORT
assert not CIBLE.exists() and not CIBLE.with_name(CIBLE.name + ".sha256").exists()

# Entrée 4, recopiée du rapport (point 4), seul emplacement : l'empreinte du rapport.
lignes_rapport = RAPPORT.read_text(encoding="utf-8").splitlines()
modele = [l for l in lignes_rapport if l.startswith("   `- **Contre-lecture 4 (finale, texte rempli)** — sous-agent neuf")]
assert len(modele) == 1
entree4 = modele[0].strip()
assert entree4.startswith("`") and entree4.endswith("`")
entree4 = entree4[1:-1]
assert entree4.count("<EMPREINTE DU RAPPORT>") == 1
entree4 = entree4.replace("<EMPREINTE DU RAPPORT>", SHA_RAPPORT)

# 1. copie à l'octet
shutil.copyfile(BROUILLON, CIBLE)
assert hashlib.sha256(CIBLE.read_bytes()).hexdigest() == SHA_BROUILLON
texte = CIBLE.read_text(encoding="utf-8")
fin_nl = texte.endswith("\n")
L = texte.split("\n")
# 3. ligne 76
assert L[75] == f"| F-3 | entropie racine des graines | {MARQUEUR_F3} |", L[75]
L[75] = f"| F-3 | entropie racine des graines | {entropie} |"
# 4. ligne 442
assert L[441].startswith("- **Contre-lecture 4 (finale, texte rempli)** — À REMPLIR :")
assert L[441].endswith("versée avec l'empreinte du texte scellé.")
L[441] = entree4
CIBLE.write_text("\n".join(L), encoding="utf-8")
assert CIBLE.read_text(encoding="utf-8").endswith("\n") == fin_nl

# 5. comparaison par programme
d = subprocess.run(["diff", str(BROUILLON), str(CIBLE)], capture_output=True, text=True)
blocs = [l for l in d.stdout.splitlines() if l and l[0].isdigit()]
print("diff:", blocs)
assert blocs == ["76c76", "442c442"], blocs

# 6. validateur : cas sain et deux artefacts (R5)
p_sain = prereg.problemes(CIBLE)
print("sain:", p_sain)
assert p_sain == []
art.mkdir(parents=True, exist_ok=True)
a1 = art / "artefact-entropie-ouverte.md"
L1 = list(L); L1[75] = f"| F-3 | entropie racine des graines | {MARQUEUR_F3} |"
a1.write_text("\n".join(L1), encoding="utf-8")
a2 = art / "artefact-entree4-sans-empreinte-rapport.md"
L2 = list(L); L2[441] = entree4.replace(f"Rapport : `{RAPPORT}`, empreinte `{SHA_RAPPORT}`", f"Rapport : `{RAPPORT}`")
assert L2[441] != entree4
a2.write_text("\n".join(L2), encoding="utf-8")
p1, p2 = prereg.problemes(a1), prereg.problemes(a2)
print("artefact 1:", p1)
print("artefact 2:", p2)
assert p1 == ["marqueur À REMPLIR restant hors des sections exigées"], p1
assert p2 == ["contre-lecture 4 sans ses deux empreintes (brouillon relu et rapport)"], p2
cellules = [c.strip() for c in __import__("re").compile(r"^\|\s*F-3\s*\|[^|]*\|([^|]*)\|\s*$", 2 | 8).findall(CIBLE.read_text(encoding="utf-8"))]
assert cellules == [entropie], cellules
print("cellule F-3 conforme au motif du code de lecture")
sha = prereg.sceller_prereg(CIBLE)
print("SCELLE", CIBLE, sha)
print("diff_sortie_complete_sha256", hashlib.sha256(d.stdout.encode()).hexdigest())
(art / "diff-brouillon14-texte-scelle.txt").write_text(d.stdout, encoding="utf-8")
