"""Candidat 3 de T0.6 = candidat 2 + les couples de découplage (6), de puissance v3 (4) et de longueurs (2) (copiés à l'octet dans ce
dossier ; appliqués dans cet ordre, chaque « ancien » unique au moment de son application), puis les substitutions E01 et suivantes
(`substitutions-candidat3-v1.json`). Décision de Lazar R-1654 (découplage). Valeurs calculées ici : {HEURE} (`date -u`), empreintes des pièces
({SHA_C2}, {SHA_DEC}, {SHA_PUI}, {SHA_LON}, {SHA_CTRL_*}). Bibliothèque standard ; aucun réseau, aucune clé. Journal à côté.

    python3 -I -B appliquer-candidat3-v1.py RACINE_DU_DEPOT
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ICI = Path(__file__).resolve().parent
C2, SHA_C2 = "brouillons/T0.6-organismes-v0-v1-candidat2.md", "72dd336336d3ad0be279ed499d214b868569d0466dfb740f50af08f8830e11eb"
C3 = "brouillons/T0.6-organismes-v0-v1-candidat3.md"
COUPLES = ("T0.6-couples-decouplage-v1.json", "T0.6-couples-puissance-v3-v1.json", "T0.6-couples-longueurs-v1.json")
ATTENDUS = {"COMMIT_CODE_T06", "EMPREINTES_CODE_T06", "EMPREINTE_AMORCE_T06", "TESTS_ATTENDUS_T06", "VALEURS_CITEES_T06"}
CLES = ["Entropie", "Commit du code d'analyse", "Configuration de T0.6 (empreinte canonique)", "Tâches d'évaluation de T0.6", "Tests attendus",
        "Chemin de la configuration de T0.6", "Chemin des tâches d'évaluation de T0.6", "Chemin des tâches de distillation de T0.6", "Chemin des consignes de P3"]


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def appliquer(texte, ident, ancien, nouveau, attendu, journal):
    n = texte.count(ancien)
    if n != attendu:
        raise SystemExit(f"{ident} : « ancien » trouvé {n} fois, {attendu} attendu : arrêt, rien d'écrit")
    journal.append(f"| {ident} | {texte[: texte.index(ancien)].count(chr(10)) + 1} | {attendu} | {len(ancien)} | {len(nouveau)} |")
    return texte.replace(ancien, nouveau)


def main(racine: Path) -> int:
    c2 = racine / C2
    if sha(c2) != SHA_C2:
        raise SystemExit("candidat 2 : empreinte non conforme")
    sortie = racine / C3
    if sortie.exists():
        raise SystemExit(f"{sortie} existe déjà (R12)")
    for nom in COUPLES:                                                    # copies à l'octet des sources du dossier brouillons/
        src = racine / "brouillons" / nom
        if src.is_file() and src.read_bytes() != (ICI / nom).read_bytes():
            raise SystemExit(f"{nom} : copie des pièces ≠ source")
    maintenant = datetime.now(timezone.utc)
    rempl = {"{HEURE}": maintenant.strftime("%H:%M"), "{SHA_C2}": SHA_C2, "{SHA_DEC}": sha(ICI / COUPLES[0]), "{SHA_PUI}": sha(ICI / COUPLES[1]),
             "{SHA_LON}": sha(ICI / COUPLES[2]), "{SHA_CTRL_SH}": sha(racine / "scripts/controle_lecture_t06_v1.sh"),
             "{SHA_CTRL_PY}": sha(racine / "scripts/controle_lecture_t06_v1.py"), "{SHA_CTRL_TEST}": sha(racine / "tests/test_t06_controle_lecture.py")}
    texte = c2.read_text(encoding="utf-8")
    journal = ["| couple ou substitution | ligne | occurrences | longueur ancien | longueur nouveau |", "|---|---|---|---|---|"]
    for nom in COUPLES:
        for c in json.loads((ICI / nom).read_text(encoding="utf-8"))["couples"]:
            texte = appliquer(texte, f"{nom.split('-')[2]}/{c['id']}", c["ancien"], c["nouveau"], 1, journal)
    subs = json.loads((ICI / "substitutions-candidat3-v1.json").read_text(encoding="utf-8"))["substitutions"]
    for s in subs:
        a, n = s["ancien"], s["nouveau"]
        for k, v in rempl.items():
            a, n = a.replace(k, v), n.replace(k, v)
        texte = appliquer(texte, s["id"], a, n, int(s.get("occurrences", 1)), journal)
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
    sortie.write_text(texte, encoding="utf-8")
    j = [f"# Journal du candidat 3 de T0.6 — {maintenant.strftime('%Y-%m-%dT%H:%M:%SZ')} (`date -u`)", "",
         f"- candidat 2 : `{C2}`, `{SHA_C2}` (vérifiée avant tout)",
         *[f"- couples : `{n}`, `{sha(ICI / n)}` (copie à l'octet dans ce dossier)" for n in COUPLES],
         f"- substitutions : `substitutions-candidat3-v1.json`, `{sha(ICI / 'substitutions-candidat3-v1.json')}`, {len(subs)} substitutions",
         f"- script : `appliquer-candidat3-v1.py`, `{sha(__file__)}`", "", *journal, "",
         f"Marqueurs du candidat 3 (`<<[A-Z0-9_]+>>`), {len(marqueurs)} distincts (occurrences) :", "", *[f"- `{m}` : {texte.count(f'<<{m}>>')}" for m in marqueurs], "",
         "Clés lues par la chaîne (une fois chacune au plus ; « Tests attendus » exactement 1) :", "", *[f"- « {k} : ` » : {n}" for k, n in comptes_c.items()], "",
         f"- résultat : `{C3}`, `{sha(sortie)}`, {texte.count(chr(10)) + 1} lignes"]
    (ICI / "journal-candidat3-v1.md").write_text("\n".join(j) + "\n", encoding="utf-8")
    print("\n".join(j))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
