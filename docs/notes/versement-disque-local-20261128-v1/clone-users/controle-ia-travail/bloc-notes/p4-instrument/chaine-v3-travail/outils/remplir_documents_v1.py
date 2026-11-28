"""Outil de travail du correcteur de la chaîne v3 : remplit les gabarits des notes et du rapport à partir des fichiers
finaux (empreintes calculées ici, jamais recopiées à la main). Les notes d'abord ; puis le rapport, qui cite l'empreinte
des notes. N'écrit que sous …/chaine-v3/ (deux fichiers neufs : refus s'ils existent, R12).
Usage : python3 -I -B remplir_documents_v1.py FIN"""
import hashlib, re, sys
from pathlib import Path

sys.dont_write_bytecode = True
P = Path("/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument")
H, W = P / "chaine-v3", P / "chaine-v3-travail"
V2 = P / "chaine-v2"
FIN = sys.argv[1]
C = "3521ff75c316c9f31403486fc6ca84a1c29daeca"
TETE = "0a44ee6139b14887fc38da8db429a46d41b300d4"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


SHA_PAIRES = sha(H / "paires-candidat2-chaine-v3-v1.json")
SHA_CANDIDAT = sha(W / "c-essai-2/travail/P4-instrument-v1-candidat2-essai.md")
assert SHA_CANDIDAT == "79c3e67756c48fd3193b9f835363e57874df6471bf93297919b9886bd160ab73"

# rapports : nom, source dans le bloc-notes (None : à venir)
SOURCES = [
    ("contre-lecture-R2-P4-instrument-brouillon1-v1.md", "contre-lecture-R2-P4-instrument-brouillon1-v1.md"),
    ("traitement-R2-P4-instrument-brouillon1-v1.md", "traitement-R2-P4-instrument-brouillon1-v1.md"),
    ("traitement-gemini-014-P4-instrument-v1.md", "traitement-gemini-014-P4-instrument-v1.md"),
    ("verification-corrections-brouillons2-3-P4-v1.md", "verification/verification-corrections-brouillons2-3-P4-v1.md"),
    ("traitement-verification-P4-instrument-v1.md", "traitement-verification-P4-instrument-v1.md"),
    ("contre-lecture-3-P4-instrument-candidat1-v1.md", "contre-lecture-3/contre-lecture-3-P4-instrument-candidat1-v1.md"),
    ("relecture-chaine-depense-P4-instrument-v1.md", "relecture-chaine-depense/relecture-chaine-depense-v1.md"),
    ("relecture-chaine-donnees-P4-instrument-v1.md", "relecture-chaine-donnees/relecture-chaine-donnees-v1.md"),
    ("relecture-chaine-fidelite-P4-instrument-v1.md", "relecture-chaine-fidelite/relecture-chaine-fidelite-v1.md"),
    ("traitement-CL3-et-relectures-chaine-P4-v1.md", "traitement-CL3-et-relectures-chaine-P4-v1.md"),
    ("verification-module-v2-contournement-P4-instrument-v1.md", "verification-module-v2-contournement/verification-module-v2-contournement-v1.md"),
    ("verification-module-v2-fidelite-P4-instrument-v1.md", "verification-module-v2-fidelite/verification-module-v2-fidelite-v1.md"),
    ("traitement-verifications-module-v2-P4-v1.md", "traitement-verifications-module-v2-P4-v1.md"),
    ("verification-module-v3-P4-instrument-v1.md", "verification-module-v3/verification-module-v3-v1.md"),
    ("verification-chaine-v2-depense-P4-instrument-v1.md", "verification-chaine-v2-depense/verification-chaine-v2-depense-v1.md"),
    ("verification-chaine-v2-donnees-P4-instrument-v1.md", "verification-chaine-v2-donnees/verification-chaine-v2-donnees-v1.md"),
    ("verification-chaine-v2-fidelite-P4-instrument-v1.md", None),
    ("traitement-verifications-chaine-v2-P4-v1.md", "traitement-verifications-chaine-v2-P4-v1.md"),
    ("verification-chaine-v3-P4-instrument-v1.md", None),
    ("verification-candidat2-P4-instrument-v1.md", None),
    ("P4-instrument-v1-brouillon1.md", "P4-instrument-v1-brouillon1.md"),
    ("P4-instrument-v1-brouillon2.md", "P4-instrument-v1-brouillon2.md"),
    ("P4-instrument-v1-brouillon3.md", "P4-instrument-v1-brouillon3.md"),
    ("P4-instrument-v1-brouillon4.md", "P4-instrument-v1-brouillon4.md"),
    ("P4-instrument-v1-candidat1.md", "P4-instrument-v1-candidat1.md"),
    ("P4-instrument-v1-candidat2.md", None),
]
# contrôle : même ordre que RAPPORTS_NOMS du module commun, empreintes égales à celles de la paire 11
src = (H / "verifications_p4_v1.py").read_text(encoding="utf-8")
noms_module = re.findall(r'^    "([A-Za-z0-9._-]+\.md)",', src.split("RAPPORTS_NOMS = (")[1].split("\n)\n")[0], re.M)
assert noms_module == [n for n, _ in SOURCES], "ordre de RAPPORTS_NOMS"
paire11 = __import__("json").loads((H / "paires-candidat2-chaine-v3-v1.json").read_text(encoding="utf-8"))[10]["nouveau"]
lignes_r = ["| n° | nom sous `prereg/contre-lectures/` | source du bloc-notes | sha256 (paire 11) |", "|---|---|---|---|"]
for k, (n, s) in enumerate(SOURCES, 1):
    if s is None:
        e = "<empreinte au versement>"
        lignes_r.append(f"| {k} | `{n}` | à venir | `{e}` |")
    else:
        e = sha(P / s)
        comp = P / (s + ".sha256")
        if comp.exists():
            assert comp.read_text().split()[0] == e, f"sceau de {s}"
        lignes_r.append(f"| {k} | `{n}` | `…/{s}` | `{e}` |")
    assert f"`prereg/contre-lectures/{n}` (`{e}`)" in paire11, f"paire 11 : {n}"
TABLE_RAPPORTS = "\n".join(lignes_r)

JOURNAUX = ["banc-arret-p4-v1.log", "banc-surveillance-p4-v1.log", "banc-traces-p4-v1.log", "banc-verifications-p4-v1.log",
            "banc-lanceur-p4-v1.log", "banc-controles-p4-v1.log", "banc-scellement-p4-v1.log", "repetition-jouet-p4-v1.log"]
def n_conformes(f):
    return sum("CONFORME" in x and "NON CONFORME" not in x for x in Path(f).read_text(encoding="utf-8").split("\n"))


V2_CONF = {j: n_conformes(V2 / j) for j in JOURNAUX if j != "repetition-jouet-p4-v1.log"}
lignes_j = ["| journal | sha256 | lignes « CONFORME » (v2) | dernière ligne |", "|---|---|---|---|"]
for j in JOURNAUX:
    t = (H / j).read_text(encoding="utf-8").rstrip("\n").split("\n")
    n = n_conformes(H / j)
    cellule = "— (répétition)" if j == "repetition-jouet-p4-v1.log" else f"{n} ({V2_CONF[j]})"
    lignes_j.append(f"| `{j}` | `{sha(H / j)}` | {cellule} | {t[-1]} |")
TABLE_JOURNAUX = "\n".join(lignes_j)
PREUVES = (W / "final/preuves.txt").read_text(encoding="utf-8").rstrip("\n")
REPETITION = (W / "final/repetition-verif.txt").read_text(encoding="utf-8").rstrip("\n")
cites = {}
for x in (PREUVES + "\n" + REPETITION).split("\n"):
    s, e = x.split()
    cites[s] = e
EGALITE = "oui, " + str(len(cites)) + " scripts" if all(sha(H / s) == e for s, e in cites.items()) else "NON"
assert EGALITE.startswith("oui")

SCRIPTS = sorted(p.name for p in H.iterdir() if p.suffix in (".sh", ".py"))
assert len(SCRIPTS) == 21
lignes_s = ["| script | sha256 (v3) | v2 |", "|---|---|---|"]
for s in SCRIPTS:
    etat = "inchangé" if sha(V2 / s) == sha(H / s) else f"changé (`{sha(V2 / s)[:12]}…`)"
    lignes_s.append(f"| `{s}` | `{sha(H / s)}` | {etat} |")
TABLE_SCRIPTS = "\n".join(lignes_s)

CONSTATS = (W / "brouillons/constats.md").read_text(encoding="utf-8").rstrip("\n")
RESERVES = (W / "brouillons/reserves.md").read_text(encoding="utf-8").rstrip("\n")
RESULTATS = (W / "brouillons/resultats.md").read_text(encoding="utf-8").rstrip("\n").replace("{TABLE_JOURNAUX}", TABLE_JOURNAUX)

commun = {"{FIN}": FIN, "{SHA_PAIRES}": SHA_PAIRES, "{SHA_CANDIDAT}": SHA_CANDIDAT, "{C}": C, "{TETE}": TETE,
          "{CONSTATS}": CONSTATS}


def remplir(gabarit, valeurs, sortie):
    t = (W / "brouillons" / gabarit).read_text(encoding="utf-8")
    for k, v in valeurs.items():
        t = t.replace(k, v)
    reste = re.findall(r"\{[A-Z_]+\}", t)
    assert not reste, reste
    s = H / sortie
    if s.exists():
        raise SystemExit(f"{s} existe déjà (R12)")
    s.write_text(t, encoding="utf-8")
    print(sortie, sha(s))


remplir("NOTES-CHAINE-v3.gabarit.md", {**commun, "{TABLE_RAPPORTS}": TABLE_RAPPORTS, "{TABLE_JOURNAUX}": TABLE_JOURNAUX,
                                        "{PREUVES}": PREUVES, "{REPETITION}": REPETITION, "{EGALITE}": EGALITE,
                                        "{TABLE_SCRIPTS}": TABLE_SCRIPTS}, "NOTES-CHAINE-v3.md")
fichiers = sorted(p.name for p in H.iterdir() if p.is_file() and not p.name.endswith(".sha256")
                  and p.name != "RAPPORT-CORRECTION-v1.md")
TABLE_FICHIERS = "\n".join(["| fichier | sha256 |", "|---|---|"] + [f"| `{f}` | `{sha(H / f)}` |" for f in fichiers])
remplir("RAPPORT-CORRECTION-v1.gabarit.md", {**commun, "{RESULTATS}": RESULTATS, "{RESERVES}": RESERVES,
                                              "{TABLE_FICHIERS}": TABLE_FICHIERS}, "RAPPORT-CORRECTION-v1.md")
print(f"fichiers dans la table du rapport : {len(fichiers)}")
