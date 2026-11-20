"""Épreuve de `controler_registre_candidat_v1.py` : un cas sain et des artefacts (R5).
Usage : python eprouver_controle_candidat_v1.py REGISTRE_DE_MAIN ARBRE_RELANCES ARBRE_LECTURE DOSSIER_DES_CANDIDATS."""
import subprocess
import sys
from pathlib import Path

base = Path(sys.argv[1]).read_text(encoding="utf-8")
relances, lecture, dossier = sys.argv[2], sys.argv[3], Path(sys.argv[4])
dossier.mkdir(parents=True, exist_ok=True)
controle = Path(__file__).parent / "controler_registre_candidat_v1.py"
assert base.endswith("\n")
V2 = "d116bf78bb2084b2d4f406535a6c6f0a23179efe"
DEBUT = ("mot de Lazar GO-2026-11-20-51 ; écarts accordés GO-2026-11-20-59 (2) et GO-2026-11-20-60 (2) ; additif 1 scellé "
         "prereg/barreau5-sabotage-ou-empreinte-adaptateurs-tenus-a-l-ecart-v1-additif-1-relance-six-instances-v3.md sha256 "
         + "0123456789abcdef" * 4)
FIN = "cumul commun relevé 18.47 USD ; enveloppe GO-2026-11-19-87 non employée"
MENTION = f"code des relances commit {V2}"
CONTENU = "GO-2026-11-19-86 ; instances 1,2,3,4,5,7"


def ligne(contenu=CONTENU, ref=f"{DEBUT} ; {MENTION} ; {FIN}", instant="2026-11-20T16:30:00Z"):
    return f"| GO-RELANCE-FORMATION-B5F | {instant} | {contenu} | {ref} |\n"


CAS = [
    ("sain", "cas sain : registre de main plus la ligne proposée (§ 4 de l'additif v3)", base + ligne(), 0),
    ("mention-absente", "artefact : mention du code des relances absente", base + ligne(ref=f"{DEBUT} ; {FIN}"), 1),
    ("mention-en-double", "artefact : mention en double", base + ligne(ref=f"{DEBUT} ; {MENTION} ; {MENTION} ; {FIN}"), 1),
    ("instance-6", "artefact : instance 6 citée", base + ligne(contenu="GO-2026-11-19-86 ; instances 1,2,3,4,5,6"), 1),
    ("instance-6-en-plus", "artefact : sept instances, la 6 comprise",
     base + ligne(contenu="GO-2026-11-19-86 ; instances 6,1,2,3,4,5,7"), 1),
    ("autre-accord", "artefact : autre accord (enveloppe GO-2026-11-19-87)",
     base + ligne(contenu="GO-2026-11-19-87 ; instances 1,2,3,4,5,7"), 1),
    ("mots-repetes", "artefact : mots « code des relances » répétés ailleurs dans la référence",
     base + ligne(ref=f"{DEBUT} ; vérification du code des relances conforme ; {MENTION} ; {FIN}"), 1),
    ("sans-espaces", "artefact : point-virgule sans espaces autour de la mention",
     base + ligne(ref=f"{DEBUT};{MENTION};{FIN}"), 1),
    ("autre-commit", "artefact : un autre commit du code des relances (celui d'avant la contre-lecture)",
     base + ligne(ref=f"{DEBUT} ; code des relances commit a74dfb4988dbe8024d5923f95999538b248d166c ; {FIN}"), 1),
    ("commit-des-premieres-marches", "artefact : le commit de CODE-FORMATION-B5F donné pour code des relances",
     base + ligne(ref=f"{DEBUT} ; code des relances commit ef80086821db08ffab42e23310a0b880ec72b9a4 ; {FIN}"), 1),
    ("instances-partielles", "artefact : cinq instances seulement (la 7 oubliée)",
     base + ligne(contenu="GO-2026-11-19-86 ; instances 1,2,3,4,5"), 1),
    ("ordre-des-instances", "artefact : instances dans un autre ordre",
     base + ligne(contenu="GO-2026-11-19-86 ; instances 7,1,2,3,4,5"), 1),
    ("cle-neuve", "artefact : une clé neuve en plus de la ligne",
     base + f"| CODE-RELANCE-FORMATION-B5F | 2026-11-20T16:29:00Z | commit {V2} | |\n" + ligne(), 1),
    ("ligne-en-double", "artefact : la ligne de relance inscrite deux fois",
     base + ligne() + ligne(instant="2026-11-20T16:31:00Z"), 1),
    ("sans-ligne", "artefact : registre de main sans la ligne de relance", base, 1),
    ("instant-anterieur", "artefact : ligne datée d'avant GO-FORMATION-B5F",
     base + ligne(instant="2026-11-20T00:42:05Z"), 1),
]
echecs = 0
for nom, quoi, texte, attendu in CAS:
    f = dossier / f"registre-candidat-{nom}.md"
    f.write_text(texte, encoding="utf-8")
    p = subprocess.run([sys.executable, str(controle), str(f), relances, lecture], capture_output=True, text=True)
    verdict = "ACCEPTÉ" in p.stdout and p.returncode == 0
    ok = (p.returncode == attendu) and (verdict == (attendu == 0)) and ("REFUSÉ" in p.stdout) == (attendu == 1)
    echecs += not ok
    print(f"--- {quoi}\n    code de sortie {p.returncode} (attendu {attendu}) : {'conforme' if ok else 'NON CONFORME'}")
    for l in p.stdout.strip().splitlines():
        print("    " + l)
# arbres échangés, arbre unique, fichier absent : le contrôle refuse aussi
sain = dossier / "registre-candidat-sain.md"
for quoi, args in (("artefact : arbres échangés", [str(sain), lecture, relances]),
                   ("artefact : le même arbre deux fois", [str(sain), relances, relances]),
                   ("artefact : fichier candidat absent", [str(dossier / "absent.md"), relances, lecture]),
                   ("artefact : deux arguments", [str(sain), relances])):
    p = subprocess.run([sys.executable, str(controle), *args], capture_output=True, text=True)
    ok = p.returncode == 1 and "REFUSÉ" in p.stdout and "ACCEPTÉ" not in p.stdout
    echecs += not ok
    print(f"--- {quoi}\n    code de sortie {p.returncode} (attendu 1) : {'conforme' if ok else 'NON CONFORME'}")
    print("    " + p.stdout.strip().splitlines()[-1])
print(f"\n{len(CAS) + 4} cas joués, {echecs} non conforme(s)")
sys.exit(1 if echecs else 0)
