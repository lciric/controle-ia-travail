"""Candidat 6 de T0.6 = candidat 5 (empreinte vérifiée avant tout) + onze couples (`T0.6-couples-candidat5-vers-candidat6-v1.json`, appliqués
dans l'ordre, chaque « ancien » unique au moment de son application) : amorce v5 à clonage réduit, lanceur v7 (R-1676, R-1677). Les valeurs
calculées ({DATE_C6}, {HEURE_C6} par `date -u`, empreintes des pièces de l'amorce v5 et du lanceur v7 lues dans l'arbre de développement) sont remplies ici.
Bibliothèque standard ; aucun réseau, aucune clé. Journal à côté.

    python3 -I -B appliquer-candidat6-v1.py RACINE_DU_DEPOT RACINE_DE_L_ARBRE_DU_LANCEUR_V7
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C5, SHA_C5 = "brouillons/T0.6-organismes-v0-v1-candidat5.md", "b67bfed30b8ea92f7cfc63211f482f5eccdac6eb2f707e2b1662de7e3949b088"
C6 = "brouillons/T0.6-organismes-v0-v1-candidat6.md"
COUPLES = "T0.6-couples-candidat5-vers-candidat6-v1.json"
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]
PIECES = {"{SHA_AMORCE5}": "scripts/amorce_instance_t06_v5.sh", "{SHA_LANCER7}": "scripts/lancer_t06_v7.sh", "{SHA_S6}": "src/controle_ia/t06/session_v6.py",
          "{SHA_RAPPORT7}": "docs/notes/g0-deux-semaines-v1/rapport-developpeur-lanceur-T0.6-v7.md", "{SHA_TESTA}": "tests/test_t06_v5_amorce.py",
          "{SHA_TESTL}": "tests/test_t06_v7_scripts.py", "{SHA_BANC7}": "scripts/banc_mutations_t06_v7.py", "{SHA_ESSAI}": "scripts/essai_amorce_t06_v5.sh",
          "{SHA_E17}": "scripts/epreuve_e1_t06_v7.sh", "{SHA_E2V4}": "brouillons/ordres-t06-e2-e3-v4/ordre-fille-6-t06-e2-v4.md",
          "{SHA_E3V4}": "brouillons/ordres-t06-e2-e3-v4/ordre-fille-6-t06-e3-v4.md",
          "{SHA_TESTC}": "tests/test_t06_cibles_invisibles_v1.py", "{SHA_ESSAIJ}": "docs/notes/g0-deux-semaines-v1/essai-amorce-t06-v5-journal.md"}


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(racine: Path, arbre: Path) -> int:
    c5 = racine / C5
    if sha(c5) != SHA_C5:
        raise SystemExit("candidat 5 : empreinte non conforme")
    sortie = racine / C6
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    maintenant = datetime.now(timezone.utc)
    rempl = {"{DATE_C6}": maintenant.strftime("%Y-%m-%d"), "{HEURE_C6}": maintenant.strftime("%H:%M"), "{SHA_C5}": SHA_C5}
    for k, chemin in PIECES.items():
        rempl[k] = sha(arbre / chemin)
    texte = c5.read_text(encoding="utf-8")
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
    if texte.count("`scripts/amorce_instance_t06_v5.sh` (`") != 1:
        raise SystemExit("forme de citation de l'amorce ≠ 1")
    if "creation <OFFRE>" in texte or texte.count("lancer_t06_v7.sh creation auto") < 1 or "`scripts/amorce_instance_t06_v4.sh` (`<<" in texte:
        raise SystemExit("creation <OFFRE> subsiste, creation auto v7 absent ou amorce v4 encore citée sous la forme lue par controles")
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 6 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 5 : `{C5}`, `{SHA_C5}` (vérifiée avant tout)",
         f"- couples : `{COUPLES}`, `{sha(ICI / COUPLES)}`, {len(couples)} couples",
         f"- script : `appliquer-candidat6-v1.py`, `{sha(__file__)}`", "",
         "Pièces du lanceur v6 citées (empreintes lues dans l'arbre de développement) :", "", *[f"- `{c}` : `{rempl[k]}`" for k, c in PIECES.items()], "",
         *journal, "", f"Marqueurs du candidat 6 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "",
         *[f"- `{m}` : {texte.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne (une fois chacune au plus ; « Tests attendus » exactement 1) :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- `creation <OFFRE>` : 0 occurrence ; `creation auto` : {texte.count('creation auto')} occurrence(s)",
         f"- résultat : `{C6}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat6-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()))
