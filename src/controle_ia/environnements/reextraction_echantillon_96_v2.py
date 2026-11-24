"""Version 2 (2026-11-24) : essai de la consigne d'enveloppe v2 sur les 16 papiers de l'échantillon d'octobre. Copie de
`reextraction_echantillon_96_v1.py` qui prend la consigne v2 par `extraire_banque_dose_reponse_v2` ; la lecture des avis
(recopiée de `rejeu_contre_verification_banque_v1.lire`, sans changement de fond) contrôle les fichiers épinglés de la
v2. Contre-vérification inchangée (consigne v1 du contre-vérificateur).

Texte d'origine de l'en-tête :

Second diagnostic : réextraction, aujourd'hui, des 16 papiers de l'échantillon de l'extraction des 96, puis
contre-vérification par le même contre-vérificateur.

But (mot de Lazar relayé par la mère, routine, 2026-11-24 : aucune règle changée, aucune dépense). Le modèle d'octobre
était le même qu'aujourd'hui. Le premier rejeu (`rejeu_contre_verification_banque_v1`) a montré que le juge
d'aujourd'hui accepte les énoncés d'octobre (0 sur 16). Reste à séparer « papiers neufs » et « conditions d'extraction
d'aujourd'hui ». Si les énoncés réextraits aujourd'hui sur les papiers d'octobre passent, la cause est dans les papiers
neufs ; s'ils échouent, elle est dans l'extraction d'aujourd'hui.

Même consigne d'enveloppe scellée, mêmes invites, même script, même validation (`extraction.lire_sorties`, accord du
script scellé), même contre-vérification (lecture de `rejeu_contre_verification_banque_v1.lire`). Les textes sont ceux
régénérés par le premier rejeu, recontrôlés contre l'empreinte du corpus du 6 octobre (R11). Ce qui porte du texte des
papiers reste sous `donnees/` ; `diag/` ne reçoit que codes, motifs et compteurs.

    python -m controle_ia.environnements.reextraction_echantillon_96_v2 preparer --run-id R --travail W --textes T
    … valider --run-id R --retours donnees/R/retours-extraction.json
    … preparer-contre-verification --run-id R
    … lire --run-id R --retours donnees/R/retours-contre-verification.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from ..gardes import GardeArret
from ..manifeste import creer_manifeste, lire_manifeste, verifier_resultat
from ..scellement import empreinte
from . import extraction as ex
from . import extraire_banque_dose_reponse_v2 as eb
from . import rejeu_contre_verification_banque_v1 as rj


def _textes(racine: Path, textes: str, ech: list[str]) -> dict[str, str]:
    """Textes des 16 papiers, contrôlés contre l'empreinte du corpus du 6 octobre (R11)."""
    fiches = {f"{f['id']}v{f['version']}": f for f in verifier_resultat(racine, racine / rj.CORPUS_96)["resultat"]["fiches"]
              if f["statut"] == "gardé"}
    out = {}
    for pid in ech:
        octets = (racine / textes / f"{pid}.md").read_bytes()
        if eb._sha(octets) != fiches[pid]["texte_sha256"]:
            raise GardeArret(f"{pid} : texte différent du corpus du 6 octobre (R11)")
        out[pid] = octets.decode("utf-8")
    return out


def _scelles(racine: Path) -> dict:
    return eb.fichiers_scelles(racine, eb.Chemins(corpus="-", textes="-"))


def _ouvrir(racine: Path, run_id: str) -> dict:
    m, _ = lire_manifeste(eb._manifeste(racine, run_id))
    if _scelles(racine) != m["config"]["fichiers_scelles"]:
        raise GardeArret("procédure, invites, scripts ou modules changés depuis l'ouverture du diagnostic")
    if empreinte(Path(__file__).resolve()) != m["config"]["module"]:
        raise GardeArret("module du diagnostic changé depuis l'ouverture")
    return m


def preparer(racine: Path, run_id: str, travail: Path, textes: str, commande: str, effort: str | None = None) -> dict:
    racine = Path(racine)
    travail = eb._hors_depot(racine, Path(travail))
    base = travail / "extraction"
    if base.exists():
        raise GardeArret(f"{base} existe déjà (R12)")
    ech = rj._resultat_96(racine, "echantillon-contre-verification")["echantillon"]
    ronde = rj._resultat_96(racine, "contre-verification-ronde-1")
    t = _textes(racine, textes, ech)
    config = {"tache": "second diagnostic : réextraction aujourd'hui des 16 papiers de l'échantillon des 96, puis "
                       "contre-vérification", "run_96": rj.RUN_96, "echantillon": ech, "textes": textes,
              "fichiers_scelles": _scelles(racine), "module": empreinte(Path(__file__).resolve()),
              "modele_sous_agents": "modèle de la session, nommé explicitement à l'appel (demande de la mère) ; "
                                    "identifiant non écrit dans le dépôt (consigne de la plateforme)",
              "effort_sous_agents": (f"fixé à « {effort} » à l'appel de chaque sous-agent (extraction et "
                                     "contre-vérification)" if effort else
                                     "non fixé à l'appel, comme à l'extraction de la banque ; valeur non lisible "
                                     "depuis la session"),
              "travail": str(travail), "racine": str(racine.resolve())}
    creer_manifeste(racine, run_id, config, [], commande=commande)
    modele = eb.consigne_extracteur_v2(racine)       # version 2 de la consigne (CV2-1)
    papiers = {}
    for pid in ech:
        d = base / pid
        papiers[pid] = eb._dossier_agent(racine, eb.Chemins(), ex.copie_de_lecture(t[pid]), d, modele,
                                         "verifier_sortie")
        (d / "sorties").mkdir()
        if eb.MARQUE_V2 not in (d / "consigne.txt").read_text(encoding="utf-8"):
            raise GardeArret(f"{pid} : consigne.txt sans l'étape 2b de la version 2")
    resultat = {"travail": str(base), "papiers": papiers,
                "verdicts_octobre": {p: ronde["papiers"][p]["motifs"] for p in ech}}
    eb._ecrire(racine, run_id, "preparation-extraction", resultat)
    return resultat


def valider(racine: Path, run_id: str, retours: dict) -> dict:
    """Validation officielle des sorties réextraites, comme `extraire_t05.valider` (anomalies, accord du script scellé
    sur entrées intactes, archive scellée des octets empreintés)."""
    racine = Path(racine)
    m = _ouvrir(racine, run_id)
    prep = verifier_resultat(racine, racine / "diag" / run_id / "preparation-extraction.json")["resultat"]
    eb._exiger_retours(retours, list(prep["papiers"]))
    t = _textes(racine, m["config"]["textes"], m["config"]["echantillon"])
    script = racine / eb.Chemins().dossier_procedure / eb.FICHIERS_PROCEDURE["verifier_sortie"]
    fiches, details, membres = {}, {}, []
    for pid, info in sorted(prep["papiers"].items()):
        d = Path(info["dossier"])
        modifiees = eb._entrees_modifiees(d, info["entrees"])
        r = ex.lire_sorties(d / "sorties", t[pid])
        if not modifiees:
            codes_script = eb.codes_du_script(script, d)
            eb.exiger_accord_script(pid, codes_script, [ex.code_anomalie(a) for a in r["anomalies"]])
        anomalies = r["anomalies"] + ([f"[entrees.modifiees] entrées modifiées : {modifiees}"] if modifiees else [])
        for nom in ex.NOMS_SORTIES:
            chemin = d / "sorties" / f"{nom}.json"
            if chemin.is_file():
                octets = chemin.read_bytes()
                if eb._sha(octets) != r["empreintes"][nom]:
                    raise GardeArret(f"{pid} : {nom}.json modifié pendant la validation")
                membres.append((f"reextraction/{pid}/{nom}.json", octets))
        fiches[pid] = {"anomalies": [ex.code_anomalie(a) for a in anomalies], "alertes": r["alertes"],
                       "theory_only": not anomalies and r["theory_only"], "empreintes": r["empreintes"],
                       "retour": eb.retour_sans_texte(retours[pid], bool(anomalies))}
        details[pid] = {"anomalies": anomalies, "derniere_ligne": retours[pid]["derniere_ligne"]}
    sha_archive = eb.archiver(racine / "donnees" / run_id / "sorties-reextraction.tar", membres)
    sha_details = eb.ecrire_donnees(racine, run_id, "details-validation-reextraction", {"papiers": details})
    resultat = {"papiers": fiches, "invalides": sorted(p for p, f in fiches.items() if f["anomalies"]),
                "theory_only": sorted(p for p, f in fiches.items() if f["theory_only"]),
                "archive_sorties_sha256": sha_archive, "details_sha256": sha_details}
    eb._ecrire(racine, run_id, "validation-reextraction", resultat)
    return resultat


def preparer_contre_verification(racine: Path, run_id: str) -> dict:
    """Dossiers des contre-vérificateurs sur les sorties réextraites valides et non « theory_only » ; écrit
    `preparation-rejeu` pour que `rejeu_contre_verification_banque_v1.lire` juge à l'identique."""
    racine = Path(racine)
    m = _ouvrir(racine, run_id)
    v = verifier_resultat(racine, racine / "diag" / run_id / "validation-reextraction.json")["resultat"]
    prep_e = verifier_resultat(racine, racine / "diag" / run_id / "preparation-extraction.json")["resultat"]
    archive = eb.lire_archive(racine / "donnees" / run_id / "sorties-reextraction.tar", v["archive_sorties_sha256"])
    t = _textes(racine, m["config"]["textes"], m["config"]["echantillon"])
    base = Path(m["config"]["travail"]) / "contre-verification"
    if base.exists():
        raise GardeArret(f"{base} existe déjà (R12)")
    modele = (racine / eb.Chemins().dossier_procedure /
              eb.FICHIERS_PROCEDURE["consigne_contre_verificateur"]).read_text(encoding="utf-8")
    papiers = {}
    for pid, f in sorted(v["papiers"].items()):
        if f["anomalies"] or f["theory_only"]:
            continue
        a_verifier = {}
        for nom in ex.NOMS_SORTIES:
            octets = archive[f"reextraction/{pid}/{nom}.json"]
            if eb._sha(octets) != f["empreintes"][nom]:
                raise GardeArret(f"{pid} : sortie {nom}.json de l'archive ≠ empreinte validée")
            a_verifier[nom] = octets
        papiers[pid] = eb._dossier_agent(racine, eb.Chemins(), ex.copie_de_lecture(t[pid]), base / pid, modele,
                                         "verifier_avis", a_verifier)
    resultat = {"papiers": papiers, "verdicts_octobre": prep_e["verdicts_octobre"],
                "hors_contre_verification": sorted(set(v["papiers"]) - set(papiers))}
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
    ap = argparse.ArgumentParser(prog="python -m controle_ia.environnements.reextraction_echantillon_96_v2")
    sous = ap.add_subparsers(dest="commande", required=True)
    s = sous.add_parser("preparer")
    s.add_argument("--run-id", required=True)
    s.add_argument("--travail", required=True)
    s.add_argument("--textes", required=True)
    s.add_argument("--effort", help="effort fixé à l'appel des sous-agents, déclaré au manifeste")
    for nom in ("valider", "lire"):
        s = sous.add_parser(nom)
        s.add_argument("--run-id", required=True)
        s.add_argument("--retours", required=True)
    s = sous.add_parser("preparer-contre-verification")
    s.add_argument("--run-id", required=True)
    a = ap.parse_args(argv)
    racine = Path(".")
    if a.commande == "preparer":
        r = preparer(racine, a.run_id, Path(a.travail), a.textes,
                     "python -m controle_ia.environnements.reextraction_echantillon_96_v2 " + " ".join(argv),
                     effort=a.effort)
        print(json.dumps({p: i["invite_agent"] for p, i in r["papiers"].items()}, ensure_ascii=False, indent=0))
    elif a.commande == "valider":
        r = valider(racine, a.run_id, eb._retours(racine, a.run_id, a.retours))
        print(json.dumps({k: r[k] for k in ("invalides", "theory_only")}, ensure_ascii=False))
    elif a.commande == "preparer-contre-verification":
        r = preparer_contre_verification(racine, a.run_id)
        print(json.dumps({p: i["invite_agent"] for p, i in r["papiers"].items()}, ensure_ascii=False, indent=0))
    else:
        _ouvrir(racine, a.run_id)
        r = lire(racine, a.run_id, eb._retours(racine, a.run_id, a.retours))
        print(json.dumps({k: r[k] for k in ("illisibles", "echecs", "echecs_octobre", "motifs")}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(_main(sys.argv[1:]))
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        sys.exit(1)
