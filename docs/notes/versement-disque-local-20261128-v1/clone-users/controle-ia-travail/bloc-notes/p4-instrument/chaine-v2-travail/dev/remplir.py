# Outil de travail (non versé) : remplit les gabarits des notes et du rapport avec les empreintes et les résultats
# finaux, écrit NOTES-CHAINE-v2.md et RAPPORT-CORRECTION-v1.md (noms neufs, R12) et leurs sceaux.
# Usage : python -B remplir.py DOSSIER_DE_FINALISATION VERDICT_FICHIER CONSTATS_JSON
import hashlib
import json
import re
import sys
from pathlib import Path

import os
H = Path(os.environ.get("H_ESSAI", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2"))
T = Path(os.environ.get("T_ESSAI", "/tmp/claude-0/-home-user/50508bff-8fed-5fe9-beef-07f1bdcaf615/scratchpad/p4-instrument/chaine-v2-travail"))
DEV = T / "dev"
FIN, VERDICT, CONSTATS = Path(sys.argv[1]), Path(sys.argv[2]).read_text(encoding="utf-8").strip(), json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
CHAINE = """verifications_p4_v1.py controles_avant_depense_p4_v1.sh lancer_p4_v1.sh sceller_p4_v1.sh surveiller_p4_v1.sh
        controle_cinq_minutes_p4_v1.sh arreter_p4_v1.sh recuperation_p4_v1.sh controler_traces_p4_v1.sh
        repetition_jouet_p4_v1.sh repetition_finale_p4_v1.sh essais_lanceur_p4_v1.sh essais_controles_p4_v1.sh
        essais_scellement_p4_v1.sh essais_surveillance_p4_v1.sh essais_arret_p4_v1.sh essais_traces_p4_v1.sh
        essais_verifications_p4_v1.sh outils_essais_p4_v1.py amorce_instance_p4_v1.sh p4_instance_v1.sh""".split()
JOURNAUX = ["banc-arret-p4-v1.log", "banc-surveillance-p4-v1.log", "banc-traces-p4-v1.log", "banc-verifications-p4-v1.log",
            "banc-lanceur-p4-v1.log", "banc-controles-p4-v1.log", "banc-scellement-p4-v1.log", "repetition-jouet-p4-v1.log"]
NEUFS = {"arreter_p4_v1.sh", "controler_traces_p4_v1.sh", "essais_arret_p4_v1.sh", "essais_traces_p4_v1.sh"}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sceller(p: Path) -> str:
    e = sha(p)
    (p.parent / (p.name + ".sha256")).write_text(f"{e}  {p.name}\n", encoding="utf-8")
    return e


v1 = {l.split()[1].rsplit("/", 1)[-1]: l.split()[0] for l in (T / "empreintes-chaine-v1-de-depart.txt").read_text(encoding="utf-8").splitlines()
      if re.fullmatch(r"[0-9a-f]{64}  \S+", l)}
lignes = ["| script | sha256 (v2) | v1 |", "|---|---|---|"]
for s in CHAINE:
    e = sha(H / s)
    assert (H / (s + ".sha256")).read_text(encoding="utf-8") == f"{e}  {s}\n", s
    etat = "neuf" if s in NEUFS else ("inchangé" if v1.get(s) == e else "changé")
    lignes.append(f"| `{s}` | `{e}` | {etat} |")
empreintes = "\n".join(lignes)
jl = ["| journal | sha256 | dernière ligne |", "|---|---|---|"]
for j in JOURNAUX:
    p = H / j
    der = [x for x in p.read_text(encoding="utf-8").splitlines() if x.strip()][-1]
    jl.append(f"| `{j}` | `{sha(p)}` | {der} |")
journaux = "\n".join(jl)
rep = (H / "repetition-jouet-p4-v1.log").read_text(encoding="utf-8")
c_essai = re.search(r"^commit du code répété : ([0-9a-f]{40})$", rep, re.M).group(1)
cand = re.search(r"^candidat répété : (\S+) ([0-9a-f]{64})$", rep, re.M)
paires = sha(H / "paires-candidat2-chaine-v2-v1.json")
code_preuves = re.search(r"code (\d+)", (FIN / "preuves-code.txt").read_text(encoding="utf-8")).group(1)
code_rep = re.search(r"code (\d+)", (FIN / "repetition-code.txt").read_text(encoding="utf-8")).group(1)
journaux += (f"\n\n`verifications_p4_v1.py preuves` (sept journaux des bancs) : code {code_preuves} ; sortie :\n\n```\n"
             + (FIN / "preuves.txt").read_text(encoding="utf-8").strip() + "\n```\n\n`verifications_p4_v1.py repetition` : code "
             + code_rep + " ; sortie :\n\n```\n" + (FIN / "repetition.txt").read_text(encoding="utf-8").strip() + "\n```\n\n"
             + "Empreintes citées par les journaux (« script éprouvé », « script répété ») comparées aux scripts de la chaîne v2 :\n\n```\n"
             + (FIN / "empreintes-citees.txt").read_text(encoding="utf-8").strip() + "\n```\n")
notes = (DEV / "notes-gabarit.md").read_text(encoding="utf-8")
for k, x in (("@@paires@@", paires), ("@@c_essai@@", c_essai), ("@@candidat@@", cand.group(2)), ("@@journaux@@", journaux),
             ("@@empreintes@@", empreintes)):
    notes = notes.replace(k, x)
assert "@@" not in notes
pn = H / "NOTES-CHAINE-v2.md"
assert not pn.exists(), "R12"
pn.write_text(notes, encoding="utf-8")
sceller(pn)
# rapport
textes = json.loads((DEV / "textes-a-ajouter.json").read_text(encoding="utf-8"))
tx = []
for i, t in enumerate(textes, 1):
    if t["mode"] == "remplacement":
        tx.append(f"{i}. {t['source']} — remplacer l'ancre :\n\n```\n{t['ancre']}\n```\n\npar :\n\n```\n{t['texte']}\n```\n")
    else:
        tx.append(f"{i}. {t['source']} — ajouter, juste après l'ancre qui finit par « …{t['ancre'][-60:].strip()} » :\n\n```\n{t['texte']}\n```\n")
res = []
for j in JOURNAUX:
    t = (H / j).read_text(encoding="utf-8")
    n = len(re.findall(r" ; CONFORME$| : CONFORME$", t, re.M))
    res.append(f"- `{j}` : {[x for x in t.splitlines() if x.strip()][-1]} ({n} lignes « CONFORME »).")
res.append(f"- Preuves : code {code_preuves}. Répétition : code {code_rep}. C d'essai `{c_essai}` ; candidat d'essai "
           f"`{cand.group(1)}` (`{cand.group(2)}`).")
fich = ["| fichier | sha256 |", "|---|---|"]
for p in sorted(H.iterdir()):
    if p.is_file() and not p.name.endswith(".sha256") and p.name != "RAPPORT-CORRECTION-v1.md":
        fich.append(f"| `{p.name}` | `{sha(p)}` |")
cst = "\n".join(f"- **{c['id']}** ({c['gravite']}) : {c['texte']}" for c in CONSTATS)
rapport = (DEV / "rapport-gabarit.md").read_text(encoding="utf-8")
for k, x in (("@@verdict@@", VERDICT), ("@@c_essai@@", c_essai), ("@@paires@@", paires), ("@@code_preuves@@", code_preuves),
             ("@@code_repetition@@", code_rep), ("@@resultats@@", "\n".join(res)), ("@@constats@@", cst),
             ("@@textes@@", "\n".join(tx)), ("@@fichiers@@", "\n".join(fich)),
             ("@@heure@@", __import__("datetime").datetime.now(__import__("datetime").timezone.utc).strftime("%H:%M"))):
    rapport = rapport.replace(k, x)
assert "@@" not in rapport
pr = H / "RAPPORT-CORRECTION-v1.md"
assert not pr.exists(), "R12"
pr.write_text(rapport, encoding="utf-8")
print(json.dumps({"notes": sha(pn), "rapport": sceller(pr), "c_essai": c_essai,
                  "candidat": cand.group(0), "paires": paires}, ensure_ascii=False))
