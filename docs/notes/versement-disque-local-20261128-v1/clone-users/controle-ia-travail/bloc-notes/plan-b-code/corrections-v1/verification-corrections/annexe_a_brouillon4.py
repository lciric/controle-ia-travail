"""Vérification (5) : annexe A du brouillon 4 = RS1.txt octet pour octet. Extraction indépendante, puis la garde du code
(cas sain) et deux artefacts (un caractère changé ; retrait manquant). Lancer avec PYTHONPATH=<clone>/src, python -B."""
import hashlib, sys
from pathlib import Path
B4 = Path(sys.argv[1]); RS1 = Path(sys.argv[2]); TMP = Path(sys.argv[3])
octets = B4.read_bytes()
lignes = octets.split(b"\n")
debut = [i for i, l in enumerate(lignes) if l == b"    ## Scoring Rubric"]
fin = [i for i, l in enumerate(lignes) if l.startswith(b"    - Do not write any analysis.")]
print("lignes de début :", [i + 1 for i in debut], "; lignes de fin :", [i + 1 for i in fin])
bloc = lignes[debut[0]:fin[-1] + 1]
assert all(not l or l.startswith(b"    ") for l in bloc)
extrait = b"\n".join(l[4:] for l in bloc) + b"\n"
attendu = RS1.read_bytes()
print("extrait :", len(extrait), "octets", hashlib.sha256(extrait).hexdigest())
print("RS1.txt :", len(attendu), "octets", hashlib.sha256(attendu).hexdigest())
print("égal octet pour octet :", extrait == attendu)
print("espaces de fin de ligne dans le bloc :", sum(1 for l in bloc if l != l.rstrip(b" \t")))
print("non ASCII dans l'extrait :", sum(1 for c in extrait if c > 127), "; retours chariot :", extrait.count(b"\r"))
from controle_ia.environnements import rubrique_simplifiee as rs
from controle_ia.gardes import GardeArret
print("cas sain, exiger_annexe_a_egale_a_rs1 :", rs.exiger_annexe_a_egale_a_rs1(B4))
texte = B4.read_text(encoding="utf-8")
for nom, altere in [("un caractère", texte.replace("SPECIFICITY: <score>", "SPECIFICITY: <score >", 1)),
                    ("retrait manquant", texte.replace("\n    ## Scoring Rubric\n", "\n   ## Scoring Rubric\n", 1)),
                    ("ligne vide en plus", texte.replace("\n    ## Scoring Rubric\n", "\n    ## Scoring Rubric\n\n", 1))]:
    assert altere != texte
    p = TMP / "artefact.md"; p.write_text(altere, encoding="utf-8")
    try:
        rs.exiger_annexe_a_egale_a_rs1(p); print("artefact", nom, ": ACCEPTÉ (défaut)")
    except GardeArret as e:
        print("artefact", nom, ": arrêt :", e)
    p.unlink()
