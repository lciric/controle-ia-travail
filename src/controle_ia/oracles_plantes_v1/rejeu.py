"""Rejeu complet sans appel de modèle (racines d'essai seulement ; aucune banque réelle n'est produite dans le lot B1).

    PYTHONPATH=src python -m controle_ia.oracles_plantes_v1.rejeu --racine <entier> --sortie <dossier>

Construit la banque (12 mondes, 312 plantés), écrit et scelle définitions servies et clés, recharge les clés par leur
empreinte, applique la batterie exacte à la banque entière, écrit le compte de P8 (100 % des faux tôt tués, 0 % des
vérités tuées, 0 % des pièges tués sous N, témoins conformes), la sous-banque S/N (servie et clé), la base
« grammaire aléatoire » et un manifeste. Code de sortie : 0 si conforme ; 3 si A1 est violée ; 4 si A1 tient mais
qu'un autre écart est relevé (témoin non conforme, redite parmi les énoncés analysables plantés) ; 1 sur toute autre
garde d'arrêt.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from ..gardes import GardeArret, etat_git
from ..manifeste import config_canonique, versions
from ..scellement import empreinte, sceller
from . import VERSION
from .banque import construire_banque
from .base_aleatoire import tirer_base
from .cles import charger_cle, ecrire_monde, fragments_de_cle, octets_json, verifier_absence_fuite
from .graines import description, generateur
from .parametres import charger
from .sous_banque import identifiants_opaques, tirer_sous_banque
from .tests_de_mort import appliquer_batterie, sortie_de_texte, verifier_instance

RACINE_DEPOT = Path(__file__).resolve().parents[3]


def rejouer_batterie_banque(mondes: list, cles: list[dict]) -> dict:
    """Applique la batterie à chaque énoncé planté lu dans les clés ; rend le rapport P8 par monde et au total."""
    total = {k: {"plantes": 0, "tues": 0} for k in ("VERITE_PLANTEE", "FAUX_TOT", "PIEGE", "TEMOIN_TRIVIAL",
                                                   "TEMOIN_GROSSIER")}
    ecarts, par_monde, t6 = [], [], {"verifies": 0, "non_verifies": 0}
    redites = {"analysables": 0, "temoins": 0}
    for m, cle in zip(mondes, cles):
        anterieures = []
        compte = {k: 0 for k in total}
        for p in cle["plantes"]:
            et = p["etiquette"]
            r = appliquer_batterie(sortie_de_texte(p["texte"]), m, anterieures=anterieures)
            tue = r.statut == "morte"
            total[et]["plantes"] += 1
            total[et]["tues"] += int(tue)
            compte[et] += int(tue)
            if r.statut == "vivante":
                redites["temoins" if et.startswith("TEMOIN") else "analysables"] += int(r.redite)
                if r.redite and not et.startswith("TEMOIN"):
                    ecarts.append(f"redite parmi les énoncés analysables plantés ({cle['identifiant_monde']} / {p['gabarit']})")
                anterieures.append(r.forme)
            ident = f"{cle['identifiant_monde']} / {p['gabarit']}"
            if et == "VERITE_PLANTEE" and (tue or not r.vraie_bornee):
                ecarts.append(f"A1 : vérité tuée ou non vraie-bornée ({ident})")
            if et == "FAUX_TOT" and not tue:
                ecarts.append(f"A1 : faux tôt vivant ({ident})")
            if et == "PIEGE" and tue:
                ecarts.append(f"A1 : piège tué sous N ({ident})")
            if et == "TEMOIN_TRIVIAL" and (tue or not r.triviale):
                ecarts.append(f"témoin trivial non conforme ({ident})")
            if et == "TEMOIN_GROSSIER" and not tue:
                ecarts.append(f"témoin grossier non conforme ({ident})")
            if et in ("FAUX_TOT", "PIEGE"):
                st, _ = verifier_instance(m.analyser(p["texte"]), m, p["instance"], m.borne_verification())
                t6["verifies" if st == "verifie" else "non_verifies"] += 1
                if st != "verifie":
                    ecarts.append(f"T6 : instance de la clé non vérifiée ({ident})")
        par_monde.append({"identifiant_monde": cle["identifiant_monde"], "famille": cle["famille"], "tues": compte})
    pct = {k: (f"{v['tues']}/{v['plantes']}") for k, v in total.items()}
    return {"total": total, "tues_sur_plantes": pct, "par_monde": par_monde, "autocontrole_t6_instances_de_cle": t6,
            "redites_parmi_plantes_vivantes": redites, "ecarts": ecarts}


def violations_a1(rapport: dict) -> list[str]:
    return [e for e in rapport["ecarts"] if e.startswith("A1") or e.startswith("T6")]


def _ecrire(chemin: Path, obj) -> str:
    if chemin.exists():
        raise GardeArret(f"{chemin} existe déjà : R12 interdit d'écraser")
    chemin.write_bytes(octets_json(obj))
    return sceller(chemin)


def executer(racine: int, sortie: str | Path) -> tuple[int, dict]:
    params, sha_params = charger()
    sortie = Path(sortie)
    if sortie.exists() and any(sortie.iterdir()):
        raise GardeArret(f"{sortie} n'est pas vide : R12 interdit d'écraser")
    sortie.mkdir(parents=True, exist_ok=True)
    banque = construire_banque(racine, params)
    ids = identifiants_opaques(generateur(racine, 3, 0), len(banque), "monde-")
    chemins_cles, empreintes = [], {}
    for (m, plantes), ident in zip(banque, ids):
        d = sortie / "mondes" / f"{m.indice:02d}-{ident}"
        ch_def, ch_cle = ecrire_monde(d, m, ident, plantes, params["statut"])
        chemins_cles.append(ch_cle)
        for ch in (ch_def, ch_cle):
            empreintes[str(ch.relative_to(sortie))] = empreinte(ch)
    cles = [charger_cle(c) for c in chemins_cles]
    rapport = rejouer_batterie_banque([m for m, _ in banque], cles)
    rapport["plantes_total"] = sum(len(c["plantes"]) for c in cles)
    rapport["mondes"] = len(cles)
    viol = violations_a1(rapport)
    rapport["A1_violee"] = bool(viol)
    rapport["temoins_conformes"] = not any(e.startswith("témoin") for e in rapport["ecarts"])
    # sous-banque S/N
    servie, cle_sb = tirer_sous_banque(banque, ids, racine, params["sous_banque"])
    o_servie = octets_json(servie)
    for c in cles:
        verifier_absence_fuite(o_servie, [f for f in fragments_de_cle(c) if f.isupper() or f.startswith("{")], "sous-banque servie")
    for nom, obj in (("sous-banque-servie-v1.json", servie), ("sous-banque-cle-v1.json", cle_sb)):
        empreintes[nom] = _ecrire(sortie / nom, obj)
    # base « grammaire aléatoire »
    base = []
    for m, _ in banque:
        textes = tirer_base(generateur(racine, 9, m.indice), m, params["base_aleatoire"])
        for t in textes:
            r = appliquer_batterie(sortie_de_texte(t), m)
            base.append({"identifiant_monde": ids[m.indice], "enonce": t, "statut": r.statut,
                         "vraie_bornee": r.vraie_bornee, "triviale": r.triviale,
                         "issues": [i.en_dict() for i in r.issues]})
    resume_base = {s: sum(1 for b in base if b["statut"] == s) for s in ("informe", "morte", "vivante")}
    resume_base["vivantes_vraies_bornees_non_triviales"] = sum(
        1 for b in base if b["statut"] == "vivante" and b["vraie_bornee"] and not b["triviale"])
    empreintes["base-grammaire-aleatoire-v1.json"] = _ecrire(sortie / "base-grammaire-aleatoire-v1.json",
                                                             {"version": VERSION, "resume": resume_base, "enonces": base})
    rapport["base_grammaire_aleatoire"] = resume_base
    rapport["version"] = VERSION
    rapport["racine"] = str(racine)
    rapport["nature"] = "rejeu d'essai sur racine d'essai ; non décisif ; paramètres provisoires"
    empreintes["rapport-p8-v1.json"] = _ecrire(sortie / "rapport-p8-v1.json", rapport)
    # manifeste
    code = {p.name: empreinte(p) for p in sorted(Path(__file__).parent.glob("*.py"))}
    params_chemin = Path(__file__).with_name("parametres_provisoires_v1.json")
    code[params_chemin.name] = empreinte(params_chemin)
    reserves = []
    try:
        git = etat_git(RACINE_DEPOT)
        if not git["propre"]:
            reserves.append("arbre de travail non propre au rejeu (code du lot B1 non commité) : rejeu d'essai seulement")
        commit = git["commit"]
    except GardeArret as e:
        commit = None
        reserves.append(f"état git illisible : {e}")
    manifeste = {
        "nature": "rejeu d'essai du lot B1 (racine d'essai ; aucune banque réelle)", "version": VERSION,
        "cree_le": datetime.now(timezone.utc).isoformat(timespec="seconds"), "commit": commit, "reserves": reserves,
        "graines": description(racine), "parametres": params, "parametres_sha256": sha_params,
        "config_sha256": hashlib.sha256(config_canonique(params)).hexdigest(), "code_sha256": code,
        "versions": versions(), "sorties_sha256": empreintes,
        "commande": f"python -m controle_ia.oracles_plantes_v1.rejeu --racine {racine} --sortie {sortie}",
    }
    _ecrire(sortie / "manifeste-rejeu-v1.json", manifeste)
    code_sortie = 3 if viol else (4 if rapport["ecarts"] else 0)
    return code_sortie, rapport


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="python -m controle_ia.oracles_plantes_v1.rejeu")
    ap.add_argument("--racine", type=int, required=True)
    ap.add_argument("--sortie", required=True)
    a = ap.parse_args(argv)
    try:
        code, rapport = executer(a.racine, a.sortie)
    except GardeArret as e:
        print(f"ARRÊT : {e}", file=sys.stderr)
        return 1
    print(json.dumps({
        "racine": a.racine, "mondes": rapport["mondes"], "plantes": rapport["plantes_total"],
        "faux_tot_tues": rapport["tues_sur_plantes"]["FAUX_TOT"],
        "verites_tuees": rapport["tues_sur_plantes"]["VERITE_PLANTEE"],
        "pieges_tues_sous_N": rapport["tues_sur_plantes"]["PIEGE"],
        "temoins_triviaux_tues": rapport["tues_sur_plantes"]["TEMOIN_TRIVIAL"],
        "temoins_grossiers_tues": rapport["tues_sur_plantes"]["TEMOIN_GROSSIER"],
        "temoins_conformes": rapport["temoins_conformes"], "A1_violee": rapport["A1_violee"],
        "autocontrole_t6": rapport["autocontrole_t6_instances_de_cle"],
        "redites_parmi_plantes": rapport["redites_parmi_plantes_vivantes"],
        "base_grammaire_aleatoire": rapport["base_grammaire_aleatoire"], "code_de_sortie": code,
    }, ensure_ascii=False, indent=1))
    return code


if __name__ == "__main__":
    sys.exit(main())
