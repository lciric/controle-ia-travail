"""Applique les 15 couples de la contre-lecture de la chaîne de la course de T0.6 (v2) aux quatre pièces visées, chacune vers
un fichier NEUF (R12 : jamais d'écrasement, création exclusive). Bibliothèque standard seule ; aucune écriture hors DOSSIER_RENDU.

- Chaque fichier de couples est vérifié contre son compagnon `.sha256` ; la sortie de la contre-lecture qui donne l'empreinte de
  ses copies corrigées (`sorties/ecrire-et-eprouver-couples-v1.json`) aussi.
- Chaque pièce est lue à l'octet par `git show <commit>:<chemin>` ; son empreinte doit commencer par le préfixe que cite la
  contre-lecture (table « Verdict par pièce »).
- Couple par couple, dans l'ordre du fichier : l'« ancien » est compté (occurrences chevauchantes comprises) dans le texte
  courant de la pièce, couples précédents appliqués ; exactement une occurrence, sinon arrêt et constat : AUCUNE pièce écrite,
  le journal dit où. Puis remplacement de cette seule occurrence. Après tous les couples, chaque « nouveau » est recompté.
- Écrit les quatre pièces sous DOSSIER_RENDU/pieces-apres-couples/ et le journal sous DOSSIER_RENDU/sorties/.

Usage : python -I -B appliquer_couples_course_t06_v1.py DEPOT DOSSIER_CONTRE_LECTURE DOSSIER_RENDU
"""
from __future__ import annotations

import datetime
import hashlib
import json
import subprocess
import sys
from pathlib import Path

DEPOT, CL, RENDU = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
C7, C5 = "8cb539f9b7ecd20fab133bfffb590ca8e1fdfc63", "84a62edd30bc30f79bef69cbcc34c42c72cc8acd"
# (repère, fichier de couples, commit, chemin de la pièce, préfixe cité par la contre-lecture, nom neuf)
PIECES = [
    ("P1", "couples-ordre-course-v2-v1.json", C7,
     "docs/notes/g0-deux-semaines-v1/ordres-t06-course-v2/ordre-fille-6-t06-course-v2-brouillon.md", "9cdffc7b",
     "ordre-fille-6-t06-course-v2-brouillon-apres-couples-v1.md"),
    ("P2", "couples-devis-v3-v1.json", C7, "docs/notes/g0-deux-semaines-v1/devis-T0.6-dose-reponse-v3.md", "10965742",
     "devis-T0.6-dose-reponse-v3-apres-couples-v1.md"),
    ("P3", "couples-candidat12-r2-v1.json", C7, "brouillons/T0.6-organismes-v0-v1-candidat12-r2.md", "0d6bf1c4",
     "T0.6-organismes-v0-v1-candidat12-r2-apres-couples-v1.md"),
    ("P4", "couples-addendum-bras-b-v3-v1.json", C5,
     "docs/notes/g0-deux-semaines-v1/bras-b-v2/addendum-bras-b-v2-brouillon-v3.md", "2ec90141",
     "addendum-bras-b-v2-brouillon-v3-apres-couples-v1.md"),
]
SORTIE_CL = CL / "sorties" / "ecrire-et-eprouver-couples-v1.json"
JOURNAL = RENDU / "sorties" / "journal-appliquer-couples-course-t06-v1.txt"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def compagnon_conforme(f: Path) -> bool:
    attendu = Path(str(f) + ".sha256").read_text(encoding="utf-8").split()[0]
    return sha(f.read_bytes()) == attendu


def compter(texte: str, motif: str) -> int:
    n, i = 0, texte.find(motif)
    while i != -1:
        n, i = n + 1, texte.find(motif, i + 1)
    return n


heure = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
entete = [f"# Journal de l'application des couples de la contre-lecture de la chaîne de la course de T0.6 (v2), v1 ; {heure}",
          "# Script : scripts/appliquer_couples_course_t06_v1.py ; pièces lues par git show <commit>:<chemin> ; aucune pièce existante modifiée.",
          "# Règle : avant chaque remplacement, l'« ancien » est compté dans le texte courant de la pièce (couples précédents",
          "# appliqués) ; exactement une occurrence, sinon arrêt et constat (aucune pièce écrite).", "#"]
for nom in [p[1] for p in PIECES] + [str(SORTIE_CL.relative_to(CL))]:
    f = CL / nom
    entete.append(f"# compagnon .sha256 : {nom} {sha(f.read_bytes())} : {'conforme' if compagnon_conforme(f) else 'NON CONFORME'}")
if not all(compagnon_conforme(CL / n) for n in [p[1] for p in PIECES] + [str(SORTIE_CL.relative_to(CL))]):
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    JOURNAL.open("x", encoding="utf-8").write("\n".join(entete + ["# ARRÊT : compagnon non conforme ; rien appliqué."]) + "\n")
    raise SystemExit("compagnon .sha256 non conforme : arrêt, aucune pièce écrite")
copies_cl = json.loads(SORTIE_CL.read_text(encoding="utf-8"))

lignes, bilans, arret, n_glob = [], [], None, 0
lignes.append("n\tidentifiant\tpièce\tcompte de l'« ancien » (texte courant)\tcompte (pièce d'origine)\tligne\tappliqué\t"
              "compte du « nouveau » (pièce finale)")
resultats = {}
for rep, fichier, commit, chemin, prefixe, nom_neuf in PIECES:
    brut = subprocess.run(["git", "-C", str(DEPOT), "show", f"{commit}:{chemin}"], capture_output=True, check=True).stdout
    origine = brut.decode("utf-8")
    assert origine.encode("utf-8") == brut
    e_av = sha(brut)
    entete.append(f"# {rep} : {chemin} @ {commit[:8]} : sha256 {e_av} ; préfixe cité par la contre-lecture {prefixe} : "
                  f"{'conforme' if e_av.startswith(prefixe) else 'NON CONFORME'}")
    if not e_av.startswith(prefixe) and arret is None:
        arret = f"{rep} : empreinte {e_av[:8]} ≠ préfixe cité {prefixe}"
    couples = json.loads((CL / fichier).read_text(encoding="utf-8"))
    texte, etats = origine, []
    for c in couples:
        n_glob += 1
        n_cour, n_orig = compter(texte, c["ancien"]), compter(origine, c["ancien"])
        if arret is None and n_cour == 1:
            i = texte.find(c["ancien"])
            ligne = texte.count("\n", 0, i) + 1
            texte = texte[:i] + c["nouveau"] + texte[i + len(c["ancien"]):]
            etats.append([n_glob, c["id"], rep, n_cour, n_orig, ligne, "oui", c["nouveau"]])
        else:
            if arret is None:
                arret = f"{rep}, couple {c['id']} : « ancien » trouvé {n_cour} fois dans le texte courant"
            etats.append([n_glob, c["id"], rep, n_cour, n_orig, "-", "non", None])
    for e in etats:
        apres = compter(texte, e[7]) if e[7] is not None else "-"
        lignes.append("\t".join(str(x) for x in e[:7] + [apres]))
    resultats[rep] = (texte.encode("utf-8"), nom_neuf, e_av, copies_cl[fichier]["sha256_copie"], chemin, commit)

if arret is None:
    (RENDU / "pieces-apres-couples").mkdir(parents=True, exist_ok=True)
    for rep, (octets, nom_neuf, e_av, e_cl, chemin, commit) in resultats.items():
        with (RENDU / "pieces-apres-couples" / nom_neuf).open("xb") as f:
            f.write(octets)
        bilans.append(f"# {rep} → pieces-apres-couples/{nom_neuf} : sha256 {sha(octets)} ; copie corrigée de la contre-lecture "
                      f"{e_cl[:16]}… : {'égale' if sha(octets) == e_cl else 'DIFFÉRENTE'} ; {len(octets)} octets")
    bilans.append(f"# Bilan : {n_glob} couples, {sum(1 for l in lignes[1:] if l.split(chr(9))[6] == 'oui')} appliqués, aucun arrêt.")
else:
    bilans.append(f"# ARRÊT ET CONSTAT : {arret} ; aucune pièce écrite.")
JOURNAL.parent.mkdir(parents=True, exist_ok=True)
with JOURNAL.open("x", encoding="utf-8") as f:
    f.write("\n".join(entete + ["#"] + lignes + ["#"] + bilans) + "\n")
print(JOURNAL.read_text(encoding="utf-8"), end="")
sys.exit(0 if arret is None else 1)
