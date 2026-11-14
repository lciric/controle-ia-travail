#!/usr/bin/env python3
"""Épreuve des valeurs attendues des témoins du lecteur v2 — relecture exploratoire, règle v2.

Écrit le 14 novembre 2026 (vers 12:02 UTC, `date -u`) par le préparateur (modèle A), d'après
`engagement-avant-epreuve-v2.md`, § 6. **Aucun appel** : ce programme prépare les messages et vérifie les réponses ; les
deux relecteurs neufs (modèle C, sans outil, en sessions séparées) sont lancés à part, et leur commande exacte est
consignée au rapport de l'épreuve.

- `preparer --temoins T.json --tour N --sortie DOSSIER` : pour chaque relecteur (B1, B2), le message même que recevrait le
  lecteur de la règle — consigne v1, question, faits, catalogue (pièces épinglées, lues par l'outil du lecteur v3.1), puis
  un lot unique des 12 témoins en vue servie (fonction `vue_lecteur` de l'outil), étiquetés `E01…`, dans un ordre tiré par
  `numpy.random.SeedSequence(2026111405).spawn(6)` (enfant 2·(N−1) pour B1, 2·(N−1)+1 pour B2) ; la clé des étiquettes
  est écrite à part (jamais servie). Tout est scellé ; rien n'est écrasé.
- `verifier --temoins T.json --tour N --dossier DOSSIER` : lit `reponse-B1-tourN.txt` et `reponse-B2-tourN.txt` (scellées),
  les vérifie par les fonctions de l'outil v3.1 (`verifier_lot` : passages mot pour mot, au moins 20 caractères, catalogue
  dans la cellule du mécanisme), et compare chaque critère aux valeurs voulues (`attendu_voulu`) ; décision par la règle du
  § 6 de l'engagement : valeur **confirmée** si les deux relecteurs donnent la valeur voulue ; sur un critère porteur, tout
  désaccord demande une réécriture ; sur un critère non porteur, la valeur commune des deux relecteurs s'ils s'accordent,
  sinon « non fixée ». Rapport JSON scellé.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

ICI = Path(__file__).resolve().parent
OUTIL_V3_1 = ICI.parents[1] / "lecture-classement-v3-1" / "outil_lecteur_conception_propre_v3_1.py"
OUTIL_V3_1_SHA256 = "95bc46c1972f91e9692f3bc28d5b8643d5957cc91cd8a39c63eb47f7240dcb44"
ENTROPIE = 2026111405
RELECTEURS = ("B1", "B2")
TOURS_MAX = 3
CRITERES = ("R1", "R2", "R3", "R4", "R5", "R6", "R7", "N")


def charger_outil():
    h = hashlib.sha256(OUTIL_V3_1.read_bytes()).hexdigest()
    if h != OUTIL_V3_1_SHA256:
        raise SystemExit(f"outil v3.1 : empreinte {h[:12]}… ≠ épinglée {OUTIL_V3_1_SHA256[:12]}…")
    spec = importlib.util.spec_from_file_location("outil_v3_1_epreuve", OUTIL_V3_1)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def ordre(n: int, tour: int, rang: int) -> list[int]:
    if not 1 <= tour <= TOURS_MAX:
        raise SystemExit(f"tour {tour} hors de 1..{TOURS_MAX}")
    e = np.random.SeedSequence(ENTROPIE).spawn(2 * TOURS_MAX)[2 * (tour - 1) + rang]
    return [int(x) for x in np.random.default_rng(e).permutation(n)]


def ecrire_scelle(p: Path, texte: str) -> str:
    if p.exists() or Path(str(p) + ".sha256").exists():
        raise SystemExit(f"{p} existe déjà (R12)")
    b = texte.encode("utf-8")
    p.write_bytes(b)
    h = hashlib.sha256(b).hexdigest()
    Path(str(p) + ".sha256").write_text(f"{h}  {p.name}\n", encoding="utf-8")
    return h


def preparer(temoins: Path, tour: int, sortie: Path) -> dict:
    O = charger_outil()
    racine = O.RACINE_DEFAUT
    pieces = {k: O.lire_piece(racine, k)[0] for k in ("consigne", "question", "faits", "catalogue")}
    T = json.loads(temoins.read_text(encoding="utf-8"))["temoins"]
    vues = [O.vue_lecteur(t["fiche"])[0] for t in T]
    sortie.mkdir(parents=True, exist_ok=True)
    cle = {"temoins": {"chemin": temoins.name, "sha256": hashlib.sha256(temoins.read_bytes()).hexdigest()},
           "tour": tour, "graines": f"SeedSequence({ENTROPIE}).spawn({2 * TOURS_MAX})", "relecteurs": {}}
    for rang, B in enumerate(RELECTEURS):
        o = ordre(len(T), tour, rang)
        lot = [(f"E{r + 1:02d}", vues[i]) for r, i in enumerate(o)]
        msg = O.texte_message(pieces, lot, 1, 1)
        h = ecrire_scelle(sortie / f"message-{B}-tour{tour}.txt", msg)
        cle["relecteurs"][B] = {"enfant": 2 * (tour - 1) + rang, "etiquettes": {f"E{r + 1:02d}": T[i]["code"]
                                                                               for r, i in enumerate(o)},
                                "message_sha256": h, "octets": len(msg.encode("utf-8"))}
    ecrire_scelle(sortie / f"cle-epreuve-tour{tour}.json", json.dumps(cle, ensure_ascii=False, indent=1) + "\n")
    return cle


def verifier(temoins: Path, tour: int, dossier: Path) -> dict:
    O = charger_outil()
    cat = O.entrees_catalogue(O.lire_piece(O.RACINE_DEFAUT, "catalogue")[0])
    T = {t["code"]: t for t in json.loads(temoins.read_text(encoding="utf-8"))["temoins"]}
    cle = json.loads((dossier / f"cle-epreuve-tour{tour}.json").read_text(encoding="utf-8"))
    if cle["temoins"]["sha256"] != hashlib.sha256(temoins.read_bytes()).hexdigest():
        raise SystemExit("clé de l'épreuve : fichier de témoins différent")
    lus, anomalies = {}, {}
    for B in RELECTEURS:
        p = dossier / f"reponse-{B}-tour{tour}.txt"
        O.verifier_sceau(p)
        et = cle["relecteurs"][B]["etiquettes"]
        vue_de = {e: O.vue_lecteur(T[c]["fiche"])[0] for e, c in et.items()}
        juge_de = {e: "levier:juge" in [q.strip() for q in T[c]["fiche"]["questions_servies"]] for e, c in et.items()}
        res, an = O.verifier_lot(p.read_text(encoding="utf-8"), list(et), vue_de, juge_de, cat)
        lus[B] = {et[e]: {k: r[k]["compte"] for k in CRITERES} for e, r in res.items()}
        anomalies[B] = [{k: a.get(k) for k in ("genre", "detail")} for a in an]
    decisions, a_reecrire = {}, []
    for code, t in T.items():
        voulu, porteurs = t["attendu_voulu"], t["criteres_porteurs"]
        d = {}
        for k in CRITERES:
            v1, v2 = lus["B1"][code][k], lus["B2"][code][k]
            if v1 == voulu[k] and v2 == voulu[k]:
                d[k] = {"voulu": voulu[k], "B1": v1, "B2": v2, "decision": "confirmée", "attendu": voulu[k]}
            elif k in porteurs:
                d[k] = {"voulu": voulu[k], "B1": v1, "B2": v2, "decision": "désaccord sur un critère porteur : réécrire",
                        "attendu": None}
                a_reecrire.append(code)
            elif v1 == v2:
                d[k] = {"voulu": voulu[k], "B1": v1, "B2": v2, "decision": "non porteur : valeur commune des relecteurs",
                        "attendu": v1}
            else:
                d[k] = {"voulu": voulu[k], "B1": v1, "B2": v2, "decision": "non porteur : non fixée", "attendu": None}
        decisions[code] = d
    return {"tour": tour, "temoins": cle["temoins"], "anomalies": anomalies, "lus": lus, "decisions": decisions,
            "a_reecrire": sorted(set(a_reecrire)),
            "accord_B1_B2": {k: sum(lus["B1"][c][k] == lus["B2"][c][k] for c in T) for k in CRITERES}}


def main(argv=None) -> int:
    a = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    s = a.add_subparsers(dest="action", required=True)
    p = s.add_parser("preparer")
    p.add_argument("--temoins", required=True)
    p.add_argument("--tour", type=int, required=True)
    p.add_argument("--sortie", required=True)
    v = s.add_parser("verifier")
    v.add_argument("--temoins", required=True)
    v.add_argument("--tour", type=int, required=True)
    v.add_argument("--dossier", required=True)
    args = a.parse_args(argv)
    if args.action == "preparer":
        c = preparer(Path(args.temoins), args.tour, Path(args.sortie))
        print(json.dumps({B: {"octets": r["octets"]} for B, r in c["relecteurs"].items()}, ensure_ascii=False))
    else:
        r = verifier(Path(args.temoins), args.tour, Path(args.dossier))
        h = ecrire_scelle(Path(args.dossier) / f"resultat-epreuve-tour{args.tour}.json",
                          json.dumps(r, ensure_ascii=False, indent=1) + "\n")
        print(json.dumps({"a_reecrire": r["a_reecrire"], "accord_B1_B2": r["accord_B1_B2"], "sha256": h},
                         ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
