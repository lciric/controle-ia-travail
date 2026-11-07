"""Candidat 7 de T0.6 = candidat 6 (empreinte vérifiée avant tout) + onze couples (`T0.6-couples-candidat6-vers-candidat7-v1.json`, appliqués dans l'ordre,
chaque « ancien » unique au moment de son application) : amorce v6, lanceur v8, citations des ordres d'épreuve scellés v3 (E2 et E3) et de la contre-lecture v7
(R-1683). Les empreintes des pièces de `main` sont recalculées sur les objets git (`git show refs/remotes/origin/main:CHEMIN`) et comparées aux valeurs attendues ;
celles de l'amorce v6 et du lanceur v8 sont lues dans l'arbre de développement. Bibliothèque standard ; aucun réseau, aucune clé. Journal à côté.

    python3 -I -B appliquer-candidat7-v1.py RACINE_DU_DEPOT RACINE_DE_L_ARBRE_DU_LANCEUR_V8
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
C6, SHA_C6 = "brouillons/T0.6-organismes-v0-v1-candidat6.md", "3250b1f88f8858cdfd782a77ada38b2301fcd6a9c592a2e9a7eda4dcf1246594"
C7 = "brouillons/T0.6-organismes-v0-v1-candidat7.md"
COUPLES = "T0.6-couples-candidat6-vers-candidat7-v1.json"
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
PIECES = {"{SHA_LANCER8}": "scripts/lancer_t06_v8.sh", "{SHA_S7}": "src/controle_ia/t06/session_v7.py", "{SHA_AMORCE6}": "scripts/amorce_instance_t06_v6.sh",
          "{SHA_RAPPORT8}": "docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v8.md", "{SHA_TESTA6}": "tests/test_t06_v6_amorce.py",
          "{SHA_TESTL8}": "tests/test_t06_v8_scripts.py", "{SHA_TESTC}": "tests/test_t06_cibles_invisibles_v1.py", "{SHA_BANC8}": "scripts/banc_mutations_t06_v8.py",
          "{SHA_ESSAI6}": "scripts/essai_amorce_t06_v6.sh", "{SHA_E18}": "scripts/epreuve_e1_t06_v8.sh",
          "{SHA_E3V5}": "brouillons/ordres-t06-e2-e3-v5/ordre-fille-6-t06-e3-v5.md",
          "{SHA_ESSAIJ6}": "docs/notes/g0-deux-semaines-v1/essai-amorce-t06-v6-journal.md"}
# pièces de `main` : (chemin, empreinte attendue, relevée avant l'écriture du script)
PIECES_MAIN = {"{SHA_E2S3}": ("docs/procedures/ordre-fille-6-t06-e2-v3.md", "0d207134c192f69b56ba5fdbf41c1301d27cc94c60cf00cfcbca027419e24097"),
               "{SHA_E3S3}": ("docs/procedures/ordre-fille-6-t06-e3-v3.md", "401468d7dbe9d39c43bcd18a54ce1ec62dcfd52d41af9f675aa42c2ccc08127c"),
               "{SHA_CM3}": ("docs/procedures/couples-mere-ordres-t06-e2-e3-v3.json", "b0a1c51c5a28481bb4ebce3a3a0ce9d142e0f0a77fde0a36d01c510b1a77b74a"),
               "{SHA_CL7}": ("docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v7/contre-lecture-lanceur-T0.6-v7-v1.md",
                             "6390c3fd8afd79d8f14f7bc80cfd359bba3cd38522b9972a84fb0cb5b9ff53e8")}


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(racine: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True).stdout


def main(racine: Path, arbre: Path) -> int:
    c6 = racine / C6
    if sha(c6) != SHA_C6:
        raise SystemExit("candidat 6 : empreinte non conforme")
    sortie = racine / C7
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    commit_main = git(racine, "rev-parse", "refs/remotes/origin/main").decode().strip()
    maintenant = datetime.now(timezone.utc)
    rempl = {"{DATE_C7}": maintenant.strftime("%Y-%m-%d"), "{HEURE_C7}": maintenant.strftime("%H:%M"), "{SHA_C6}": SHA_C6, "{COMMIT_MAIN}": commit_main}
    for k, (chemin, attendu) in PIECES_MAIN.items():
        h = hashlib.sha256(git(racine, "show", f"refs/remotes/origin/main:{chemin}")).hexdigest()
        if h != attendu:
            raise SystemExit(f"{chemin} sur main : {h} ≠ attendu {attendu}")
        rempl[k] = h
    for k, chemin in PIECES.items():
        rempl[k] = sha(arbre / chemin)
    texte = c6.read_text(encoding="utf-8")
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
    if texte.count("`scripts/amorce_instance_t06_v6.sh` (`") != 1:
        raise SystemExit("forme de citation de l'amorce v6 ≠ 1")
    if "creation <OFFRE>" in texte or texte.count("lancer_t06_v8.sh creation auto") < 1 or "`scripts/amorce_instance_t06_v5.sh` (`<<" in texte:
        raise SystemExit("creation <OFFRE> subsiste, creation auto v8 absent ou amorce v5 encore citée sous la forme lue par controles")
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 7 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 6 : `{C6}`, `{SHA_C6}` (vérifiée avant tout)", f"- `main` (refs/remotes/origin/main) : `{commit_main}`",
         f"- couples : `{COUPLES}`, `{sha(ICI / COUPLES)}`, {len(couples)} couples",
         f"- script : `appliquer-candidat7-v1.py`, `{sha(__file__)}`", "",
         "Pièces de `main` recalculées sur les objets git et égales aux valeurs attendues :", "", *[f"- `{c}` : `{rempl[k]}`" for k, (c, _) in PIECES_MAIN.items()], "",
         "Pièces de l'amorce v6 et du lanceur v8 citées (empreintes lues dans l'arbre de développement) :", "", *[f"- `{c}` : `{rempl[k]}`" for k, c in PIECES.items()], "",
         *journal, "", f"Marqueurs du candidat 7 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "",
         *[f"- `{m}` : {texte.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne (une fois chacune au plus ; « Tests attendus » exactement 1) :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- `creation <OFFRE>` : 0 occurrence ; `creation auto` : {texte.count('creation auto')} occurrence(s)",
         f"- résultat : `{C7}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat7-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
