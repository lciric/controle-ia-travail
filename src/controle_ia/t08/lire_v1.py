"""Entrée en ligne de commande de la lecture de T0.8 (consigne de la chaîne de lancement v3, `6f52c4db…`, § 3.3). v1.

    python -m controle_ia.t08.lire_v1 --config <configuration de la lecture> --run-id <AAAAMMJJ-HHMMSS-nom> --prereg <texte>

1. Appelle `lecture_v1.executer_lecture(config, Path("."), run_id, prereg)`, depuis la racine du dépôt, après
   `scellement.verifier(config)` ; **aucune règle de lecture n'est écrite ici** : elles sont toutes dans `lecture_v1.py`.
2. **Échantillon de l'audit R4** (constat L-2) : après le résultat et sans le changer, si l'étape (i) a déclenché l'audit, écrit
   le fichier scellé `diag/<run>/echantillon-audit-r4-t08.json`, rattaché au manifeste de la lecture : pour les seules clés que
   le résultat désigne (`audit_R4.echantillon`), la ligne de `textes-actions-t06.jsonl` (texte de l'action), le coût lu
   (colonne `cout` de `mesures-t06.npz`), et la ligne de chacun des quatre fichiers de lectures des juges (sortie et score),
   recopiées des entrées à l'octet (lignes JSON telles quelles), entrées ouvertes par la liste blanche (empreintes contrôlées).
   Le score de chaque ligne recopiée doit égaler celui que le résultat désigne, sinon arrêt. Tirage inchangé (celui de
   `lecture_v1.py`) ; audit non déclenché : aucun fichier. Une clé hors de l'échantillon désigné est refusée.
3. **Sortie sans nombre de résultat** (constat m-L1) : la sortie standard ne porte qu'une ligne JSON de chemins et d'empreintes
   des fichiers écrits (manifeste, `lecture-t08.json`, tables D et F, échantillon ou `null`) ; la sortie d'erreur, les lignes
   `PROGRES` de `lecture_v1.py` (noms d'étapes) et les messages d'arrêt (`ARRÊT : <motif>`). Ni la ligne de la table D, ni les
   qualifications, ni la durée, que rend `executer_lecture`, ne sont imprimées. Messages d'arrêt du code qui portent un nombre
   tiré des données ou des résultats, relevés sans les changer (rapport de la chaîne) : `statistiques_v1.py` l. 31 (comptes
   d'alertes hors domaine), `tables_v1.py` l. 160 (borne de T6-10), `mots_et_cout_v1.py` l. 306, 314, 316 (centre, état et
   traits de M2 au contrôle d'identité).
Codes : 0 ; 1 sur un arrêt de garde ; 2 usage.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from ..gardes import GardeArret

COMMANDE = "python -m controle_ia.t08.lire_v1"
NOM_ECHANTILLON = "echantillon-audit-r4-t08"
LECTURES = {"J8p": "lectures_J8_une_passe", "J3p": "lectures_J3_une_passe", "J8r": "lectures_J8_raisonnement",
            "J3r": "lectures_J3_raisonnement"}


def cles_designees(resultat: dict) -> dict[str, dict]:
    """Clés que le résultat désigne pour l'audit R4 (`audit_R4.echantillon`), avec la condition et les scores désignés ;
    `{}` si l'audit n'est pas déclenché."""
    a = resultat.get("audit_R4") or {}
    if not a.get("declenche") or not a.get("echantillon"):
        return {}
    out = {}
    for condition, lignes in sorted(a["echantillon"].items()):
        for x in lignes:
            if x["cle"] in out:
                raise GardeArret(f"échantillon de l'audit : clé {x['cle']} désignée deux fois")
            out[x["cle"]] = {"condition": condition, "juges": x.get("juges") or {}}
    return out


def _lignes_brutes(chemin: Path, cles: set[str]) -> dict[str, str]:
    """Lignes JSON brutes (telles quelles, sans le saut de ligne) des clés demandées."""
    out = {}
    with open(chemin, "rb") as f:
        for brute in f:
            if not brute.strip():
                continue
            cle = json.loads(brute)["cle"]
            if cle in cles:
                if cle in out:
                    raise GardeArret(f"{chemin.name} : clé {cle} en double")
                out[cle] = brute.rstrip(b"\n").decode("utf-8")
    return out


def extraire_echantillon(resultat: dict, lb, cles_demandees=None) -> dict | None:
    """Échantillon de l'audit R4 tiré des entrées de la liste blanche `lb` (empreintes contrôlées) ; `None` si l'audit n'est
    pas déclenché. `cles_demandees` (essais) : une clé hors de l'échantillon désigné est refusée."""
    des = cles_designees(resultat)
    if cles_demandees is not None:
        hors = sorted(set(cles_demandees) - set(des))
        if hors:
            raise GardeArret(f"clé(s) hors de l'échantillon désigné par le résultat : {hors[:3]} : refus")
    if not des:
        return None
    cles = set(des if cles_demandees is None else cles_demandees)
    textes = _lignes_brutes(lb.chemin("textes_7b"), cles)
    mesures = lb.lire_npz("mesures_7b")
    cout = {str(k): (None if v != v else float(v)) for k, v in zip(mesures["cle"], mesures["cout"])}
    juges = {s: _lignes_brutes(lb.chemin(n), cles) for s, n in LECTURES.items()}
    sortie = []
    for k in sorted(cles):
        if k not in textes or k not in cout:
            raise GardeArret(f"échantillon de l'audit : clé {k} absente des textes ou des mesures de 7b")
        j = {}
        for s, lignes in juges.items():
            if k in lignes:
                score = json.loads(lignes[k]).get("score")
                if s in des[k]["juges"] and des[k]["juges"][s] != score:
                    raise GardeArret(f"échantillon de l'audit : score de {s} pour {k} ≠ celui du résultat : arrêt")
                j[s] = {"ligne": lignes[k]}
            elif s in des[k]["juges"]:
                raise GardeArret(f"échantillon de l'audit : lecture {s} de {k} désignée mais absente du fichier : arrêt")
        sortie.append({"cle": k, "condition": des[k]["condition"], "ligne_texte": textes[k], "cout_lu": cout[k], "juges": j})
    return {"cles": len(sortie), "actions": sortie,
            "fichiers": {n: lb.entrees[n]["chemin"] for n in ("textes_7b", "mesures_7b", *LECTURES.values())}}


def _main(argv: list[str]) -> int:
    import argparse

    from ..manifeste import ecrire_resultat
    from ..scellement import empreinte, verifier
    from . import entrees_v1 as en
    from .lecture_v1 import executer_lecture

    ap = argparse.ArgumentParser(prog=COMMANDE)
    ap.add_argument("--config", required=True)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--prereg", default=None)
    a = ap.parse_args(argv)
    verifier(a.config)
    config = json.loads(Path(a.config).read_text(encoding="utf-8"))
    r = executer_lecture(config, Path("."), a.run_id, a.prereg)
    lecture = Path(r["lecture"])
    sha_lecture = verifier(lecture)
    corps = json.loads(lecture.read_text(encoding="utf-8"))
    ech = extraire_echantillon(corps["resultat"], en.ListeBlanche(Path("."), config["entrees"]))
    chemin_ech = None
    if ech is not None:
        chemin_ech = ecrire_resultat(Path("."), r["manifeste"], NOM_ECHANTILLON,
                                     {**ech, "lecture_t08": {"chemin": str(lecture), "sha256": sha_lecture}})
        if verifier(lecture) != sha_lecture:
            raise GardeArret("lecture-t08.json changé par l'écriture de l'échantillon : arrêt")
    tables = Path(r["tables_d_f"])
    print(json.dumps({"manifeste": str(r["manifeste"]), "lecture": str(lecture), "lecture_sha256": sha_lecture,
                      "tables_d_f": str(tables), "tables_d_f_sha256": empreinte(tables),
                      "echantillon": str(chemin_ech) if chemin_ech else None,
                      "echantillon_sha256": empreinte(chemin_ech) if chemin_ech else None}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:                      # contre-lecture m-4 : toute autre erreur sort aussi en « ARRÊT : », sans trace
        print(f"ARRÊT : {type(e).__name__} : {e}", file=sys.stderr)
        sys.exit(1)
