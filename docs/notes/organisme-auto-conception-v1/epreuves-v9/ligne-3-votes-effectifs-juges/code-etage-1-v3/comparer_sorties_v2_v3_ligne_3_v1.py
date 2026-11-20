"""Preuve que les sorties existantes du banc v2 sont égales à l'octet en v3 (additif 1 v2, « Ce que le code doit
changer » : « toutes les clés existantes de la sortie sont égales avant et après ») — v1.

Joue `executer_etage_1` du banc v2 et du banc v3 en mode « essais » (racine 2026111930 seule), sur deux configurations
réduites, chacune dans un dossier neuf ; puis, pour chaque configuration :
  - relit le résultat du v2 et vérifie que sa ré-écriture rend ses octets (garde de la méthode) ;
  - liste les chemins de clés du v2 absents du v3 (attendu : aucun) et les chemins neufs du v3 (attendu : exactement
    les ajouts déclarés) ;
  - liste les feuilles communes dont la valeur diffère (attendu : `/version` seule, par la règle R12) ;
  - retire du v3 les chemins neufs, remet `version` à celle du v2, ré-écrit comme le banc et compare à l'octet ;
  - compare les dérivations de graines des deux manifestes (mêmes racines, tâches, clés, nombres d'enfants).
N'écrit dans le rapport que des empreintes, des chemins de clés et des booléens : aucune valeur mesurée.

Usage :
    python3 -B comparer_sorties_v2_v3_ligne_3_v1.py --banc-v2 CHEMIN --empreinte-banc-v2 HEX --banc-v3 CHEMIN \
        --travail DOSSIER_NEUF --sortie RAPPORT.json
Développeur, modèle L′.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

CONFIGURATION_D_ESSAI = {  # copie à l'identique de celle des essais v2 et v3
    "repliques": 16,
    "tirages_reechantillonnage": 30,
    "estimateur": {"J": [2, 5], "lois_J2": [1, 3], "lois_J5": [4], "profils": ["egal_0.2"], "rhos": [0.0, 0.6],
                   "n": [50]},
    "puissance": {"ecarts": [0.10], "lois": [1], "rhos": [0.0], "rhos_prime": [0.5], "n": 100},
    "ecart_rho_prime": {"ecarts": [0.3], "rhos": [0.3], "taux": 0.20, "n": 100},
    "double_rendu": {"n": [50], "s": [0.5], "deltas": [0.0, 0.5]},
    "cadrage": {"t": [20], "deltas": [0.0, 0.5], "seuils": [0.1, 0.3]},
    "alarme": {"m": [10], "suites": 40},
}
CONFIGURATION_D_ESSAI_V3 = {**CONFIGURATION_D_ESSAI, "alarme": {"m": [10, 20, 40], "suites": 400}}
CONFIGURATIONS = (("essai", CONFIGURATION_D_ESSAI), ("essai_alarme_trois_m", CONFIGURATION_D_ESSAI_V3))
CLES_NEUVES_PAR_BRAS = ("part_des_suites_en_alarme_sur_changement_a_effet", "comptes_silence_1",
                        "mention_part_des_suites_en_alarme")
CLES_NEUVES_PAR_CELLULE_D_ALARME = ("comptes_du_melange_plante",)
CLE_NEUVE_DES_CRITERES = "alarme_fcbf4a2dd1a57"


def sha256_octets(b):
    return hashlib.sha256(b).hexdigest()


def charger(nom, chemin):
    spec = importlib.util.spec_from_file_location(nom, chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom] = module
    spec.loader.exec_module(module)
    return module


def ecrire_comme_le_banc(objet):
    return (json.dumps(objet, ensure_ascii=False, indent=1, sort_keys=True, allow_nan=False) + "\n").encode("utf-8")


def chemins_seulement_dans(a, b, chemin=""):
    res = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in a:
            if k not in b:
                res.append(f"{chemin}/{k}")
            else:
                res.extend(chemins_seulement_dans(a[k], b[k], f"{chemin}/{k}"))
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            res.append(f"{chemin}[longueur]")
        for i, (x, y) in enumerate(zip(a, b)):
            res.extend(chemins_seulement_dans(x, y, f"{chemin}/{i}"))
    return res


def feuilles_differentes(a, b, chemin=""):
    """Chemins communs aux deux arbres où la valeur (ou le type) diffère ; les clés propres à un seul arbre sont
    ignorées ici (elles sont listées à part)."""
    if isinstance(a, dict) and isinstance(b, dict):
        res = []
        for k in a:
            if k in b:
                res.extend(feuilles_differentes(a[k], b[k], f"{chemin}/{k}"))
        return res
    if isinstance(a, list) and isinstance(b, list):
        res = [] if len(a) == len(b) else [f"{chemin}[longueur]"]
        for i, (x, y) in enumerate(zip(a, b)):
            res.extend(feuilles_differentes(x, y, f"{chemin}/{i}"))
        return res
    return [] if (type(a) is type(b) and a == b) else [chemin]


def retirer(objet, chemins):
    for chemin in chemins:
        parties = chemin.strip("/").split("/")
        cible = objet
        for p in parties[:-1]:
            cible = cible[int(p)] if isinstance(cible, list) else cible[p]
        del cible[parties[-1]]


def chemins_neufs_declares(n_alarme):
    return sorted(["/criteres_mecaniques/" + CLE_NEUVE_DES_CRITERES]
                  + [f"/alarme/{i}/{cle}" for i in range(n_alarme) for cle in CLES_NEUVES_PAR_CELLULE_D_ALARME]
                  + [f"/alarme/{i}/par_bras/{nom}/{cle}" for i in range(n_alarme) for nom in "ABCD"
                     for cle in CLES_NEUVES_PAR_BRAS])


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--banc-v2", required=True)
    p.add_argument("--empreinte-banc-v2", required=True)
    p.add_argument("--banc-v3", required=True)
    p.add_argument("--travail", required=True)
    p.add_argument("--sortie", required=True)
    a = p.parse_args(argv)
    travail, sortie = Path(a.travail), Path(a.sortie)
    if travail.exists() or sortie.exists():
        print("refus : dossier de travail ou sortie déjà présents", file=sys.stderr)
        return 2
    chemin_v2, chemin_v3 = Path(a.banc_v2).resolve(), Path(a.banc_v3).resolve()
    emp_v2 = sha256_octets(chemin_v2.read_bytes())
    if emp_v2 != a.empreinte_banc_v2:
        print(f"refus : empreinte du banc v2 {emp_v2}, {a.empreinte_banc_v2} attendue", file=sys.stderr)
        return 2
    v2 = charger("banc_juges_scriptes_ligne_3_v2", chemin_v2)
    v3 = charger("banc_juges_scriptes_ligne_3_v3", chemin_v3)
    travail.mkdir(parents=True)
    rapport = {"programme": "comparer-sorties-v2-v3-ligne-3-v1",
               "programme_sha256": sha256_octets(Path(__file__).resolve().read_bytes()),
               "banc_v2": str(chemin_v2), "banc_v2_sha256": emp_v2,
               "banc_v3": str(chemin_v3), "banc_v3_sha256": sha256_octets(chemin_v3.read_bytes()),
               "mode": "essais (racine 2026111930 seule)", "configurations": {}}
    tout_bon = True
    for nom, cfg in CONFIGURATIONS:
        _, man2 = v2.executer_etage_1(v2.Contexte("essais"), cfg, travail / nom / "v2")
        _, man3 = v3.executer_etage_1(v3.Contexte("essais"), cfg, travail / nom / "v3")
        octets_v2 = (travail / nom / "v2" / "resultat-etage-1-ligne-3-v2.json").read_bytes()
        octets_v3 = (travail / nom / "v3" / "resultat-etage-1-ligne-3-v3.json").read_bytes()
        lu2, lu3 = json.loads(octets_v2), json.loads(octets_v3)
        relecture = ecrire_comme_le_banc(lu2) == octets_v2
        absents = chemins_seulement_dans(lu2, lu3)
        neufs = sorted(chemins_seulement_dans(lu3, lu2))
        declares = chemins_neufs_declares(len(cfg["alarme"]["m"]))
        differentes = feuilles_differentes(lu2, lu3)
        reduit = json.loads(octets_v3)
        retirer(reduit, neufs)
        reduit["version"] = lu2["version"]
        octets_reduits = ecrire_comme_le_banc(reduit)
        egal = octets_reduits == octets_v2
        derivations = man2["graines"]["derivations"] == man3["graines"]["derivations"]
        racines = sorted({d["racine"] for d in man2["graines"]["derivations"] + man3["graines"]["derivations"]})
        bloc = {
            "configuration_sha256": v3.sha256_json(v3._nettoyer(cfg)),
            "resultat_v2_sha256": sha256_octets(octets_v2),
            "resultat_v3_sha256": sha256_octets(octets_v3),
            "resultat_v3_reduit_sha256": sha256_octets(octets_reduits),
            "relecture_du_v2_rend_ses_octets": relecture,
            "cles_du_v2_absentes_du_v3": absents,
            "cles_neuves_du_v3": neufs,
            "cles_neuves_egales_aux_ajouts_declares": neufs == declares,
            "feuilles_communes_differentes": differentes,
            "v3_reduit_egal_au_v2_a_l_octet": egal,
            "derivations_de_graines_egales": derivations,
            "racines_derivees": racines,
        }
        rapport["configurations"][nom] = bloc
        bon = (relecture and not absents and neufs == declares and differentes == ["/version"] and egal and derivations
               and racines == [2026111930])
        tout_bon = tout_bon and bon
        print(f"{nom} : relecture={relecture} absents={len(absents)} neufs={len(neufs)} "
              f"neufs_declares={neufs == declares} feuilles_differentes={differentes} egal_a_l_octet={egal} "
              f"derivations_egales={derivations} racines={racines}")
    rapport["journal_des_graines_v2"] = sorted({d["racine"] for d in v2.JOURNAL_GRAINES})
    rapport["journal_des_graines_v3"] = sorted({d["racine"] for d in v3.JOURNAL_GRAINES})
    tout_bon = tout_bon and rapport["journal_des_graines_v2"] == [2026111930] == rapport["journal_des_graines_v3"]
    rapport["toutes_les_sorties_existantes_egales"] = tout_bon
    with open(sortie, "x", encoding="utf-8") as f:
        f.write(json.dumps(rapport, ensure_ascii=False, indent=1) + "\n")
    print(f"toutes les sorties existantes égales : {tout_bon}")
    return 0 if tout_bon else 1


if __name__ == "__main__":
    sys.exit(main())
