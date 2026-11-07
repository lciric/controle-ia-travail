"""Candidat 8 de T0.6 = candidat 7 (empreinte vérifiée avant tout) + neuf couples (`T0.6-couples-candidat7-vers-candidat8-v1.json`, appliqués dans l'ordre, chaque
« ancien » unique au moment de son application) + deux remplacements globaux comptés (`lancer_t06_v8.sh` → v9 et `amorce_instance_t06_v6.sh` → v7, hors la citation
historique de la v8 et de la v6, protégée puis restaurée). Les empreintes de la v9 sont lues sur les objets git du commit du code (jamais sur un arbre de travail) ;
celles des pièces de `main` sont recalculées sur les objets de `refs/remotes/origin/main` et comparées aux préfixes attendus. Bibliothèque standard ; aucun réseau, aucune clé.

    python3 -I -B appliquer-candidat8-v1.py RACINE_DU_DEPOT RACINE_DE_L_ARBRE_DU_LANCEUR_V9 COMMIT_DU_CODE
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
C7, SHA_C7 = "brouillons/T0.6-organismes-v0-v1-candidat7.md", "a7ba0f4a595b5abd"          # préfixe ; l'empreinte complète est calculée et écrite au journal
C8 = "brouillons/T0.6-organismes-v0-v1-candidat8.md"
COUPLES = "T0.6-couples-candidat7-vers-candidat8-v1.json"
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06", "REGLE_MOTS_ET_COUT_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
PIECES = {"{SHA_AMORCE7}": "scripts/amorce_instance_t06_v7.sh", "{SHA_LANCER9}": "scripts/lancer_t06_v9.sh", "{SHA_S8}": "src/controle_ia/t06/session_v8.py",
          "{SHA_RAPPORT9}": "docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v9.md", "{SHA_TESTA7}": "tests/test_t06_v7_amorce.py",
          "{SHA_TESTL9}": "tests/test_t06_v9_scripts.py", "{SHA_TESTS9}": "tests/test_t06_v9_session.py", "{SHA_TESTN9}": "tests/test_t06_v9_nouveaux.py",
          "{SHA_TESTP9}": "tests/test_t06_v9_prix.py", "{SHA_TESTM7}": "tests/test_t06_v7_amorce_minuterie.py", "{SHA_BANC9}": "scripts/banc_mutations_t06_v9.py"}
# pièces de `main` : (chemin, préfixe attendu)
PIECES_MAIN = {"{SHA_E2V4}": ("docs/procedures/ordre-fille-6-t06-e2-v4.md", "4c1113cd"), "{SHA_E3V5}": ("docs/procedures/ordre-fille-6-t06-e3-v5.md", "db0ad520"),
               "{SHA_CME2E3V4}": ("docs/procedures/couples-mere-ordres-t06-e2-e3-v4.json", "366d69e7"),
               "{SHA_CME3V5}": ("docs/procedures/couples-mere-ordre-t06-e3-v5.json", "e80e586a"),
               "{SHA_CL8}": ("docs/notes/g0-deux-semaines-v1/contre-lecture-lanceur-T0.6-v8/contre-lecture-lanceur-T0.6-v8-v1.md", "653a5a29")}


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def git(racine: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(racine), *args], check=True, capture_output=True).stdout


def global_compte(texte: str, ancien: str, nouveau: str, attendu: int, nom: str) -> str:
    n = texte.count(ancien)
    if n != attendu:
        raise SystemExit(f"remplacement global « {nom} » : {n} occurrence(s), {attendu} attendue(s) : arrêt, rien d'écrit")
    return texte.replace(ancien, nouveau)


def main(racine: Path, arbre: Path, code: str) -> int:
    c7 = racine / C7
    if not sha(c7).startswith(SHA_C7):
        raise SystemExit("candidat 7 : empreinte non conforme")
    sortie = racine / C8
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    commit_code = git(arbre, "rev-parse", f"{code}^{{commit}}").decode().strip()
    commit_main = git(racine, "rev-parse", "refs/remotes/origin/main").decode().strip()
    maintenant = datetime.now(timezone.utc)
    rempl = {"{DATE_C8}": maintenant.strftime("%Y-%m-%d"), "{HEURE_C8}": maintenant.strftime("%H:%M"), "{SHA_C7}": sha(c7), "{COMMIT_CODE}": commit_code, "{COMMIT_MAIN}": commit_main}
    for k, (chemin, prefixe) in PIECES_MAIN.items():
        h = hashlib.sha256(git(racine, "show", f"refs/remotes/origin/main:{chemin}")).hexdigest()
        if not h.startswith(prefixe):
            raise SystemExit(f"{chemin} sur main : {h} ≠ préfixe attendu {prefixe}")
        rempl[k] = h
    for k, chemin in PIECES.items():
        rempl[k] = hashlib.sha256(git(arbre, "show", f"{commit_code}:{chemin}")).hexdigest()
    texte = c7.read_text(encoding="utf-8")
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
    # remplacements globaux comptés, hors citations historiques (v8, v6) protégées
    hist_l = "(`scripts/lancer_t06_v8.sh`, `debcfa65"
    hist_a = "(`scripts/amorce_instance_t06_v6.sh`, `78ad709f"
    texte = global_compte(texte, hist_l, hist_l.replace("v8.sh", "v8§.sh"), 1, "protection de la citation du lanceur v8")
    texte = global_compte(texte, hist_a, hist_a.replace("v6.sh", "v6§.sh"), 1, "protection de la citation de l'amorce v6")
    nl, na = texte.count("lancer_t06_v8.sh"), texte.count("amorce_instance_t06_v6.sh")
    texte = texte.replace("lancer_t06_v8.sh", "lancer_t06_v9.sh").replace("amorce_instance_t06_v6.sh", "amorce_instance_t06_v7.sh")
    texte = texte.replace("lancer_t06_v8§.sh", "lancer_t06_v8.sh").replace("amorce_instance_t06_v6§.sh", "amorce_instance_t06_v6.sh")
    journal += ["", f"- remplacements globaux : `lancer_t06_v8.sh` → v9 : {nl} ; `amorce_instance_t06_v6.sh` → v7 : {na} (citations historiques de la v8 et de la v6 protégées)"]
    if re.findall(r"\{[A-Z_0-9]+\}", texte):
        raise SystemExit(f"accolades non résolues : {sorted(set(re.findall(r'[{][A-Z_0-9]+[}]', texte)))}")
    marqueurs = sorted({m.strip("<>") for m in re.findall(r"<<[A-Z0-9_]+>>", texte)})
    if set(marqueurs) != ATTENDUS:
        raise SystemExit(f"marqueurs : {marqueurs}, attendus {sorted(ATTENDUS)}")
    lignes = texte.split("\n")
    comptes_c = {k: sum(1 for l in lignes if f"{k} : `" in l) for k in CLES}
    if comptes_c["Tests attendus"] != 1 or any(n > 1 for n in comptes_c.values()) or comptes_c["Entropie"] != 1:
        raise SystemExit(f"clés lues par la chaîne : {comptes_c}")
    if texte.count("`scripts/amorce_instance_t06_v7.sh` (`") != 1:
        raise SystemExit("forme de citation de l'amorce v7 ≠ 1")
    if "creation <OFFRE>" in texte or texte.count("lancer_t06_v9.sh creation auto") < 1:
        raise SystemExit("creation <OFFRE> subsiste ou creation auto v9 absent")
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 8 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 7 : `{C7}`, `{sha(c7)}` (vérifiée avant tout)", f"- commit du code : `{commit_code}`", f"- `main` (refs/remotes/origin/main) : `{commit_main}`",
         f"- couples : `{COUPLES}`, `{sha(ICI / COUPLES)}`, {len(couples)} couples",
         f"- script : `appliquer-candidat8-v1.py`, `{sha(__file__)}`", "",
         "Pièces de `main` recalculées sur les objets git et conformes aux préfixes attendus :", "", *[f"- `{c}` : `{rempl[k]}`" for k, (c, _) in PIECES_MAIN.items()], "",
         "Pièces de la v9 (empreintes lues sur les objets git du commit du code) :", "", *[f"- `{c}` : `{rempl[k]}`" for k, c in PIECES.items()], "",
         *journal, "", f"Marqueurs du candidat 8 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "",
         *[f"- `{m}` : {texte.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne (une fois chacune au plus ; « Tests attendus » exactement 1) :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- résultat : `{C8}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat8-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), sys.argv[3]))
