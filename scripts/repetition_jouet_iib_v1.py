"""Répétition jouet de bout en bout de (ii-b), v1 (consigne du développeur, § 3) : processeur, sans réseau, sans dépense, données
**factices** (`iib/jouet_v1`). EXPLORATOIRE, NON OPPOSABLE (R-522) ; elle éprouve la chaîne, elle ne mesure rien.

    PYTHONPATH=src python scripts/repetition_jouet_iib_v1.py preparer DOSSIER ENTROPIE
        tâches, consigne du maître et consignes de P3 factices, scellées ; configuration jouet scellée (`config-jouet-iib-v1.json`) ;
    PYTHONPATH=src python scripts/repetition_jouet_iib_v1.py jouer DOSSIER RUN_ID
        course (étalonnage, épreuves, tours, distillation sur l'élève jouet, évaluation, oracle ; `iib/lanceur_v1`), puis lecture (1),
        consignation de son empreinte dans un registre des décisions **factice** du dossier, puis lecture (2) ;
    PYTHONPATH=src python scripts/repetition_jouet_iib_v1.py comparer DOSSIER RUN_A RUN_B
        égalité à l'octet de toutes les sorties des deux jeux, hors du manifeste (horodaté), du résumé (qui porte l'empreinte du
        manifeste et la durée) et des durées ; écrit et scelle `comparaison-RUN_A-RUN_B.json`.
Le dépôt doit être propre au lancement de `jouer` (le manifeste le relève). Codes : 0 ; 1 sur toute garde ; 3 si les jeux diffèrent.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

from controle_ia.gardes import GardeArret
from controle_ia.iib import configuration_v1 as cf
from controle_ia.iib import jouet_v1 as jv
from controle_ia.iib import lanceur_v1 as la
from controle_ia.iib import lecture_v1 as lv
from controle_ia.scellement import sceller, verifier

CONFIG = "config-jouet-iib-v1.json"
REGISTRE = "registre-decisions-factice-iib-v1.md"
HORS = ("manifeste.json", "manifeste.json.sha256", "resume.json", "resume.json.sha256", "durees-iib.json", "durees-iib.json.sha256")


def preparer(dossier: Path, entropie: int) -> int:
    c = jv.preparer_monde(dossier, entropie=entropie)
    cf.exiger_config_iib_v1(c)
    f = dossier / CONFIG
    if f.exists():
        raise GardeArret(f"{f} existe déjà (R12)")
    f.write_text(json.dumps(c, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PRÉPARÉ : {f} sha256 {sceller(f)} ; entropie {entropie}")
    return 0


def jouer(dossier: Path, run_id: str) -> int:
    verifier(dossier / CONFIG)
    c = json.loads((dossier / CONFIG).read_text(encoding="utf-8"))
    resume = la.executer(c, dossier, run_id)
    l1 = lv.lecture_1(lv.charger_sorties(dossier, run_id))
    chemin1, sha1 = lv.ecrire(dossier, run_id, lv.NOM_1, l1)
    reg = dossier / REGISTRE
    with open(reg, "a", encoding="utf-8") as f:
        if reg.stat().st_size == 0:
            f.write("# Registre des décisions FACTICE de la répétition jouet de (ii-b) (jamais `registres/decisions.md`)\n\n")
        f.write(f"- lecture (1) de la répétition jouet {run_id} scellée : `{sha1}`\n")
    l2 = lv.exiger_lecture_1_consignee(dossier, run_id, reg)
    r2, mots = lv.lecture_2(lv.charger_sorties(dossier, run_id, avec_textes=True), l2["contenu"])
    r2["lecture_1"]["sha256"] = l2["sha256"]
    _, sha2 = lv.ecrire(dossier, run_id, lv.NOM_2, r2)
    _, sha_m = lv.ecrire(dossier, run_id, lv.NOM_MOTS, mots)
    print(json.dumps({"run": run_id, "acceptes": resume["acceptes"], "tours": resume["tours"], "lecture_1": l1["phrase"], "lecture_1_sha256": sha1,
                      "lecture_2_par_action": r2["phrase_par_action"], "mots_et_cout": r2["mots_et_cout"], "lecture_2_sha256": sha2,
                      "mots_sha256": sha_m}, ensure_ascii=False))
    return 0


def _fichiers(dossier: Path, run_id: str) -> dict:
    sortie = {}
    for d in ("diag", "donnees"):
        base = dossier / d / run_id
        for p in sorted(base.rglob("*")):
            if p.is_file():
                sortie[f"{d}/{p.relative_to(base).as_posix()}"] = p
    return sortie


def comparer(dossier: Path, a: str, b: str) -> int:
    fa, fb = _fichiers(dossier, a), _fichiers(dossier, b)
    if set(fa) != set(fb):
        raise GardeArret(f"ensembles de sorties différents : {sorted(set(fa) ^ set(fb))}")
    lignes, differents = {}, []
    for k in sorted(fa):
        ha, hb = hashlib.sha256(fa[k].read_bytes()).hexdigest(), hashlib.sha256(fb[k].read_bytes()).hexdigest()
        compare = Path(k).name not in HORS
        lignes[k] = {"sha256_a": ha, "sha256_b": hb, "compare": compare, "egal": ha == hb}
        if compare and ha != hb:
            differents.append(k)
    out = dossier / f"comparaison-{a}-{b}.json"
    if out.exists():
        raise GardeArret(f"{out} existe déjà (R12)")
    out.write_text(json.dumps({"avertissement": cf.AVERTISSEMENT, "jeu_a": a, "jeu_b": b, "hors_comparaison": list(HORS),
                               "fichiers": lignes, "compares": sum(v["compare"] for v in lignes.values()), "differents": differents,
                               "identiques_a_l_octet": not differents}, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(f"COMPARAISON : {sum(v['compare'] for v in lignes.values())} fichiers comparés, {len(differents)} différent(s) ; {out} sha256 {sceller(out)}")
    return 0 if not differents else 3


def main(argv: list[str]) -> int:
    try:
        if len(argv) == 3 and argv[0] == "preparer":
            return preparer(Path(argv[1]), int(argv[2]))
        if len(argv) == 3 and argv[0] == "jouer":
            return jouer(Path(argv[1]), argv[2])
        if len(argv) == 4 and argv[0] == "comparer":
            return comparer(Path(argv[1]), argv[2], argv[3])
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
