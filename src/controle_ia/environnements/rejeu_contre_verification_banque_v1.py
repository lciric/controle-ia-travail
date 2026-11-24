"""Rejeu diagnostique de la contre-vérification sur l'échantillon de l'extraction des 96 (octobre 2026).

But (accord de la mère, routine, le 2026-11-24 : aucune règle changée, aucune dépense) : séparer une dérive du juge
d'une dérive de l'extracteur, après l'arrêt de seuil de l'extraction de la banque de 64 tâches neuves (12 échecs sur 16,
tous « énoncé révélateur »). Le contre-vérificateur d'aujourd'hui juge, avec la même consigne scellée et la même
mécanique (`extraction.anomalies_avis`, `extraction.motifs_echec_avis`, script scellé `verifier-avis-v1.py`), les
16 papiers de l'échantillon de l'extraction des 96, sur leurs sorties scellées d'octobre (archive de la tentative 1,
empreintes de la validation). En octobre, ces 16 papiers avaient 0 échec.

Ce module ne modifie aucun code scellé ; il en appelle les fonctions. Les textes des 16 papiers, absents de cette
machine, sont régénérés par la chaîne scellée (`corpus_arxiv.traiter_papier`) et contrôlés contre l'empreinte du corpus
du 6 octobre (R11 : toute différence arrête). Ce qui porte du texte des papiers reste sous `donnees/` ; `diag/` ne
reçoit que codes, motifs et compteurs.

    python -m controle_ia.environnements.rejeu_contre_verification_banque_v1 preparer --run-id R --travail W --donnees D
    … lire --run-id R --retours donnees/R/retours-rejeu.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, lire_manifeste, verifier_resultat
from ..scellement import empreinte
from . import corpus_arxiv as ca
from . import corpus_arxiv_banque_dose_reponse_v1 as sel
from . import extraction as ex
from . import extraire_banque_dose_reponse_v1 as eb

RUN_96 = "20261007-082440-t05-extraction"
CORPUS_96 = "diag/20261006-134235-t05-corpus/corpus.json"


def _resultat_96(racine: Path, nom: str) -> dict:
    return verifier_resultat(racine, racine / "diag" / RUN_96 / f"{nom}.json")["resultat"]


def preparer(racine: Path, run_id: str, travail: Path, donnees: Path, commande: str) -> dict:
    racine = Path(racine)
    travail = eb._hors_depot(racine, Path(travail))
    if Path(donnees).exists() or (travail / "rejeu").exists():
        raise GardeArret("dossiers de données ou de travail déjà présents (R12)")
    ech = _resultat_96(racine, "echantillon-contre-verification")["echantillon"]
    ronde = _resultat_96(racine, "contre-verification-ronde-1")
    v1 = _resultat_96(racine, "validation-tentative-1")
    fiches = {f"{f['id']}v{f['version']}": f for f in verifier_resultat(racine, racine / CORPUS_96)["resultat"]["fiches"]
              if f["statut"] == "gardé"}
    if len(ech) != 16 or any(ronde["papiers"][p]["tentative"] != 1 for p in ech):
        raise GardeArret("échantillon des 96 : 16 papiers à la tentative 1 attendus")
    archive = eb.lire_archive(racine / "donnees" / RUN_96 / "sorties-tentative-1.tar", v1["archive_sorties_sha256"])
    # textes régénérés par la chaîne scellée, contrôlés contre l'empreinte du corpus (R11), avant le manifeste
    Path(donnees).mkdir(parents=True)
    filtre = Path(donnees) / "sans-figures.lua"
    filtre.write_text(ca.FILTRE_LUA, encoding="utf-8")
    textes = {}
    for pid in ech:
        f = fiches[pid]
        fiche = ca.traiter_papier({"id": f["id"], "version": f["version"], "titre": f["titre"]}, Path(donnees), filtre,
                                  ouvrir=sel.ouvrir_https_reprenable)
        if fiche.get("statut") != "gardé" or fiche.get("texte_sha256") != f["texte_sha256"]:
            raise GardeArret(f"{pid} : texte régénéré différent du corpus du 6 octobre (R11)")
        textes[pid] = (Path(donnees) / "textes" / f"{pid}.md").read_text(encoding="utf-8")
    config = {"tache": "rejeu diagnostique de la contre-vérification sur l'échantillon de l'extraction des 96",
              "run_96": RUN_96, "echantillon": ech, "archive_sorties_sha256": v1["archive_sorties_sha256"],
              "fichiers_scelles": eb.fichiers_scelles(racine, eb.Chemins(corpus="-", textes="-")),
              "modele_sous_agents": "modèle de la session, nommé explicitement à l'appel (demande de la mère) ; "
                                    "identifiant non écrit dans le dépôt (consigne de la plateforme)",
              "donnees": str(donnees), "travail": str(travail), "racine": str(racine.resolve()),
              "module": empreinte(Path(__file__).resolve())}
    creer_manifeste(racine, run_id, config, [], commande=commande)
    modele = (racine / eb.Chemins().dossier_procedure /
              eb.FICHIERS_PROCEDURE["consigne_contre_verificateur"]).read_text(encoding="utf-8")
    papiers = {}
    for pid in ech:
        a_verifier = {}
        for nom in ex.NOMS_SORTIES:
            octets = archive[f"tentative-1/{pid}/{nom}.json"]
            if eb._sha(octets) != v1["papiers"][pid]["empreintes"][nom]:
                raise GardeArret(f"{pid} : sortie {nom}.json de l'archive ≠ empreinte validée")
            a_verifier[nom] = octets
        papiers[pid] = eb._dossier_agent(racine, eb.Chemins(), ex.copie_de_lecture(textes[pid]),
                                         travail / "rejeu" / pid, modele, "verifier_avis", a_verifier)
    resultat = {"papiers": papiers, "verdicts_octobre": {p: ronde["papiers"][p]["motifs"] for p in ech}}
    eb._ecrire(racine, run_id, "preparation-rejeu", resultat)
    return resultat


def lire(racine: Path, run_id: str, retours: dict) -> dict:
    racine = Path(racine)
    m, _ = lire_manifeste(eb._manifeste(racine, run_id))
    if eb.fichiers_scelles(racine, eb.Chemins(corpus="-", textes="-")) != m["config"]["fichiers_scelles"]:
        raise GardeArret("procédure, invites, scripts ou modules changés depuis l'ouverture du rejeu")
    prep = verifier_resultat(racine, racine / "diag" / run_id / "preparation-rejeu.json")["resultat"]
    eb._exiger_retours(retours, list(prep["papiers"]))
    script = racine / eb.Chemins().dossier_procedure / eb.FICHIERS_PROCEDURE["verifier_avis"]
    fiches, details, membres = {}, {}, []
    for pid, info in sorted(prep["papiers"].items()):
        d = Path(info["dossier"])
        modifiees = eb._entrees_modifiees(d, info["entrees"])
        avis, anomalies = None, []
        if not (d / "avis.json").is_file():
            anomalies.append("[fichier.absent] avis.json absent")
        else:
            octets = (d / "avis.json").read_bytes()
            try:
                avis = json.loads(octets.decode("utf-8"), parse_constant=ex._refuser_constante)
                membres.append((f"rejeu/{pid}/avis.json", octets))
            except ValueError as e:
                anomalies.append(f"[json.illisible] avis.json illisible : {e}")
        h10 = cibles = None
        if not anomalies and not modifiees:
            h9, h10, cibles = (json.loads((d / "a-verifier" / f"{n}.json").read_bytes()) for n in ex.NOMS_SORTIES)
            anomalies = ex.anomalies_avis(avis, h9, h10, cibles)
        if not modifiees:
            codes_script = eb.codes_du_script(script, d)
            eb.exiger_accord_script(pid, codes_script, [ex.code_anomalie(a) for a in anomalies])
        else:
            anomalies.append(f"[entrees.modifiees] entrées modifiées : {modifiees}")
        lisible = not anomalies
        fiche = {"lisible": lisible, "codes": [ex.code_anomalie(a) for a in anomalies],
                 "retour": eb.retour_sans_texte(retours[pid], bool(anomalies)),
                 "verdict_octobre": prep["verdicts_octobre"][pid]}
        if lisible:
            fiche["motifs"] = ex.motifs_echec_avis(avis, cibles, h10)
            fiche["cibles_defectueuses"] = sum(not (t["grounded"] and t["observable"]) for t in avis["targets"])
            fiche["cibles"] = len(avis["targets"])
            fiche["classification"] = {k: avis[k] for k in ("theory_experiment_correct", "data_type_correct",
                                                             "domains_reasonable")}
            fiche["compute_plausible"] = avis["compute_plausible"]
        fiches[pid] = fiche
        details[pid] = {"anomalies": anomalies, "avis": avis if eb._encodable(avis) else None,
                        "derniere_ligne": retours[pid]["derniere_ligne"]}
    sha_archive = eb.archiver(racine / "donnees" / run_id / "avis-rejeu.tar", membres)
    sha_details = eb.ecrire_donnees(racine, run_id, "details-rejeu", {"papiers": details})
    lisibles = [f for f in fiches.values() if f["lisible"]]
    resultat = {"papiers": fiches, "illisibles": sorted(p for p, f in fiches.items() if not f["lisible"]),
                "echecs": sorted(p for p, f in fiches.items() if f["lisible"] and f["motifs"]),
                "echecs_octobre": sorted(p for p, f in fiches.items() if f["verdict_octobre"]),
                "motifs": {m_: sum(m_ in f.get("motifs", []) for f in lisibles)
                           for m_ in sorted({x for f in lisibles for x in f["motifs"]})},
                "archive_avis_sha256": sha_archive, "details_sha256": sha_details}
    eb._ecrire(racine, run_id, "lecture-rejeu", resultat)
    return resultat


def _main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.rejeu_contre_verification_banque_v1")
    sous = ap.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("preparer")
    s.add_argument("--run-id", required=True)
    s.add_argument("--travail", required=True)
    s.add_argument("--donnees", required=True)
    s = sous.add_parser("lire")
    s.add_argument("--run-id", required=True)
    s.add_argument("--retours", required=True)
    a = ap.parse_args(argv)
    racine = Path(".")
    if a.commande == "preparer":
        r = preparer(racine, a.run_id, Path(a.travail), Path(a.donnees),
                     "python -m controle_ia.environnements.rejeu_contre_verification_banque_v1 " + " ".join(argv))
        print(json.dumps({p: i["invite_agent"] for p, i in r["papiers"].items()}, ensure_ascii=False, indent=0))
    else:
        r = lire(racine, a.run_id, eb._retours(racine, a.run_id, a.retours))
        print(json.dumps({k: r[k] for k in ("illisibles", "echecs", "echecs_octobre", "motifs")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
