"""Candidat 5 de T0.6 = candidat 4 (empreinte vérifiée avant tout) + neuf couples (`T0.6-couples-candidat4-vers-candidat5-v1.json`, appliqués
dans l'ordre, chaque « ancien » unique au moment de son application) : citations des deux ordres d'épreuve scellés (`main`), du commit d'épreuve
et de la contre-lecture v6 à la place des brouillons v3 ; renvois périmés corrigés (rapports du développeur v2 à v6, branche de sortie). Les
empreintes des pièces de `main` sont recalculées ici sur les objets git (`git show origin/main:CHEMIN`) et comparées aux valeurs attendues.
Bibliothèque standard ; aucun réseau, aucune clé. Journal à côté.

    python3 -I -B appliquer-candidat5-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C4, SHA_C4 = "brouillons/T0.6-organismes-v0-v1-candidat4.md", "a81cd47ef58941e91db8e12a98353293451085828f6c18fd6d3ee34186a79a53"
C5 = "brouillons/T0.6-organismes-v0-v1-candidat5.md"
COUPLES = "T0.6-couples-candidat4-vers-candidat5-v1.json"
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
# pièces de `main` : (clé de remplacement, chemin, sha256 attendu, donné par la session mère ou lu dans la contre-lecture)
PIECES_MAIN = {"{SHA_E2S}": ("docs/procedures/ordre-fille-6-t06-e2-v1.md", "8ad0ca95f9820381ffd7bbb3760b0365aac7b93d762c104171864a93ba2c8405"),
               "{SHA_E3S}": ("docs/procedures/ordre-fille-6-t06-e3-v1.md", "97a45a31db4f18e38932fa1d41540df12421ecebb460e69ac2b40cd379e54c92"),
               "{SHA_COUPLES_MERE}": ("docs/procedures/couples-mere-ordres-t06-e2-e3-v1.json", "aad65afd3c245070882b2dab091086ba554620f974cdcd4f17754999e37a0178"),
               "{SHA_CL6}": ("docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v6/contre-lecture-lanceur-T0.6-v6-v1.md",
                             "ce610cc7081c8f474e16efd77687466c1b84b840db203aca7336caae78098340")}
COMMIT_EPREUVE = "74f59b28418a4f19dcea5d70b0c5f2c922a301fb"


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(racine: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True).stdout


def main(racine: Path) -> int:
    c4 = racine / C4
    if sha(c4) != SHA_C4:
        raise SystemExit("candidat 4 : empreinte non conforme")
    sortie = racine / C5
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    commit_main = git(racine, "rev-parse", "refs/remotes/origin/main").decode().strip()
    rempl = {}
    for k, (chemin, attendu) in PIECES_MAIN.items():
        h = hashlib.sha256(git(racine, "show", f"refs/remotes/origin/main:{chemin}")).hexdigest()
        if h != attendu:
            raise SystemExit(f"{chemin} sur main : {h} ≠ attendu {attendu}")
        rempl[k] = h
    try:                                                                   # le commit d'épreuve existe et descend de 1d226d2c
        git(racine, "merge-base", "--is-ancestor", "1d226d2cdb9d4091e025c7e1cc5f9ed322f328d5", COMMIT_EPREUVE)
    except subprocess.CalledProcessError:
        raise SystemExit("commit d'épreuve : absent ou ne descend pas de 1d226d2c")
    maintenant = datetime.now(timezone.utc)
    rempl.update({"{DATE_C5}": maintenant.strftime("%Y-%m-%d"), "{HEURE_C5}": maintenant.strftime("%H:%M"), "{SHA_C4}": SHA_C4,
                  "{COMMIT_MAIN}": commit_main})
    texte = c4.read_text(encoding="utf-8")
    journal = ["| couple | ligne | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    couples = json.loads((ICI / COUPLES).read_text(encoding="utf-8"))["couples"]
    for c in couples:
        a, n = c["ancien"], c["nouveau"]
        for k, v in rempl.items():
            a, n = a.replace(k, v), n.replace(k, v)
        if texte.count(a) != 1:
            raise SystemExit(f"{c['id']} : « ancien » trouvé {texte.count(a)} fois, 1 attendu : arrêt, rien d'écrit")
        journal.append(f"| {c['id']} | {texte[: texte.index(a)].count(chr(10)) + 1} | 1 | {len(a)} | {len(n)} |")
        texte = texte.replace(a, n)
    if re.findall(r"\{[A-Z_0-9]+\}", texte):
        raise SystemExit(f"accolades non résolues : {sorted(set(re.findall(r'[{][A-Z_0-9]+[}]', texte)))}")
    marqueurs = sorted({m.strip("<>") for m in re.findall(r"<<[A-Z0-9_]+>>", texte)})
    if set(marqueurs) != ATTENDUS:
        raise SystemExit(f"marqueurs : {marqueurs}, attendus {sorted(ATTENDUS)}")
    lignes = texte.split("\n")
    comptes_c = {k: sum(1 for l in lignes if f"{k} : `" in l) for k in CLES}
    if comptes_c["Tests attendus"] != 1 or any(n > 1 for n in comptes_c.values()) or comptes_c["Entropie"] != 1:
        raise SystemExit(f"clés lues par la chaîne : {comptes_c}")
    if texte.count("`scripts/amorce_instance_t06_v4.sh` (`") != 1:
        raise SystemExit("forme de citation de l'amorce ≠ 1")
    if "creation <OFFRE>" in texte or "ordres-t06-e2-e3-v3/ordre-fille" in texte.split("12. **Ce que le candidat 5 change**")[0].split("11. **Ce que le candidat 4 change**")[1]:
        raise SystemExit("creation <OFFRE> subsiste ou le point 11 cite encore les brouillons v3")
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 5 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 4 : `{C4}`, `{SHA_C4}` (vérifiée avant tout)",
         f"- couples : `{COUPLES}`, `{sha(ICI / COUPLES)}`, {len(couples)} couples",
         f"- script : `appliquer-candidat5-v1.py`, `{sha(__file__)}`", f"- `main` (refs/remotes/origin/main) : `{commit_main}`",
         f"- commit d'épreuve : `{COMMIT_EPREUVE}` (existe, descend de `1d226d2c`)", "",
         "Pièces de `main` recalculées sur les objets git et égales aux valeurs attendues :", "",
         *[f"- `{c}` : `{rempl[k]}`" for k, (c, _) in PIECES_MAIN.items()], "", *journal, "",
         f"Marqueurs du candidat 5 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "",
         *[f"- `{m}` : {texte.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne (une fois chacune au plus ; « Tests attendus » exactement 1) :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- résultat : `{C5}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat5-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
