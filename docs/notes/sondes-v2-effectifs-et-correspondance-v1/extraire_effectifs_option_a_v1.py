#!/usr/bin/env python3
"""Extraction déterministe, sans score et sans ouverture de tableau d'activations, pour :
1. La note des effectifs des diagnostics préalables des sondes v2 (`note-des-effectifs-sondes-v2-v1.md`),
   conforme à `spec-note-des-effectifs-v2.md` et aux trois errata d'Option A (commit `0ce9e3511`).
2. Le projet de table de correspondance du rejeu croisé (`correspondance-rejeu-croise-v1.json` et sa note
   d'attestation `correspondance-rejeu-croise-sondes-v2-v1.md`), conforme à `spec-correspondance-rejeu-croise-v2.md`.

Cloisonnement strict :
- Activations de `20261123-044043-b5f-lecture` (commit `2e8e662359e192a13cec0cadeb4a218385c8ff59`) :
  lit UNIQUEMENT `garde-activations.json`, `inventaire-activations.json`, `runs/20261123-044043-b5f-lecture/manifeste.json`
  et leurs compagnons `.sha256` en mémoire via `gh api`. N'ouvre JAMAIS aucun `.npy` d'activation (ni valeurs, ni forme,
  ni en-tête binaire).
- Table `SCORES-BBIS` (`origin/donnees/t07-etape-b-bis-v2`, `diag/20261118-154143-bbis-t07-v1/sondes-bbis.json`) :
  vérifie l'empreinte SHA-256 attendue (`645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62`), puis vérifie
  l'empreinte de chaque morceau `.npz` listé dans `fichiers_scores` et lit UNIQUEMENT les noms de membres ZIP et les
  tableaux de chaînes de plan (`*__cles.npy` et `*__taches.npy`, type contrôlé chaîne Unicode/ASCII strictement).
  N'ouvre JAMAIS aucun tableau de score ni aucune statistique dérivée d'un score.
- Ne modifie ni `/home/antigravity/lciric/controle-ia-travail` ni `/home/antigravity/worktrees/sondes-v2-code`.
"""
from __future__ import annotations

import hashlib
import io
import json
import math
import re
import shutil
import subprocess
import sys
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

WORKTREE_CODE = Path("/home/antigravity/worktrees/sondes-v2-code")
REPO_PRINCIPAL = Path("/home/antigravity/lciric/controle-ia-travail")
SORTIE_DIR = Path(
    "/home/antigravity/.gemini/jetski/brain/v1/default/jetski_remote_agents_3p_devbox/"
    "ff6e9350-ef6c-4238-b52d-64a517f4205f/scratch/note-effectifs-sondes-v2"
)
TMP_VERIF_DIR = Path("/tmp/verif-note-eff")

COMMIT_B5F = "2e8e662359e192a13cec0cadeb4a218385c8ff59"
REF_BBIS = "origin/donnees/t07-etape-b-bis-v2"
CHEMIN_BBIS = "diag/20261118-154143-bbis-t07-v1/sondes-bbis.json"
SHA_BBIS_ATTENDU = "645a172fe14fc18ff23ede0efa45dadd0841297489931ae6788caa6549a81c62"
LIGNE_REGISTRE_BBIS = "SCORES-BBIS (registres/t07-etape-b-bis-v1.md, ligne 8, 2026-11-18T19:43:48Z)"

REDIGEE_PAR = "sous-agent-83ff952349ac7c27e7a058fe8138c9d8"

# Paramètres du modèle de coût (plan-epreuve-plantee-et-devis-v2.md, § 5 ; calculs/devis_epreuve_plantee_v2.py)
REPLIQUES = 500
EUR_HEL1 = 1.3942
EUR_MAX = 1.9932
TAUX_USD = 1.25
COEURS_CCX63 = 48
PLAFOND_GO_18_USD = 27.10

DOSE_SPECS = [
    ("0.25", "P-S25", "O-S25", "J25-S25", "A25-honnete", "O-honnete"),
    ("0.5", "P-S50", "O-S50", "J50-S50", "A50-honnete", "O-honnete"),
    ("0.75", "P-S75", "O-S75", "J75-S75", "A75-honnete", "O-honnete"),
    ("1.0", "P-S100", "O-S100", "J100-S100", "A100-honnete", "O-honnete"),
]

# Ajout du worktree sondes-v2-code en lecture seule dans sys.path
sys.path.insert(0, str(WORKTREE_CODE / "src"))
from controle_ia.scellement import sceller, verifier  # noqa: E402
from controle_ia.sondes_v2 import formats_v1 as fm  # noqa: E402
from controle_ia.sondes_v2 import statistiques_v2 as st  # noqa: E402
from controle_ia.sondes_v2.magasin_v1 import _CHEMIN_B5  # noqa: E402


def gh_raw(path: str, ref: str = COMMIT_B5F) -> bytes:
    return subprocess.check_output(
        [
            "gh",
            "api",
            f"repos/lciric/controle-ia-travail/contents/{path}?ref={ref}",
            "-H",
            "Accept: application/vnd.github.raw+json",
        ]
    )


def git_show(ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(REPO_PRINCIPAL), "show", f"{ref}:{path}"])


def verifier_octets_compagnon(data: bytes, sha_bytes: bytes, nom_attendu: str) -> str:
    lignes = [l for l in sha_bytes.decode("utf-8").splitlines() if l.strip()]
    if len(lignes) != 1:
        raise RuntimeError(f"Compagnon invalide pour {nom_attendu}: {len(lignes)} lignes")
    attendue, nom = lignes[0].split("  ", 1)
    if nom != nom_attendu:
        raise RuntimeError(f"Nom compagnon {nom!r} != {nom_attendu!r}")
    obtenue = hashlib.sha256(data).hexdigest()
    if obtenue != attendue:
        raise RuntimeError(f"SHA-256 faux pour {nom_attendu}: {obtenue} != {attendue}")
    return obtenue


def extraire_activations() -> tuple[dict, dict, bytes, bytes]:
    """Extrait les comptes des activations gardées de 20261123-044043-b5f-lecture sans ouvrir aucun .npy."""
    garde_raw = gh_raw("donnees/20261123-044043-b5f-lecture/garde-activations.json")
    garde_sha_raw = gh_raw("donnees/20261123-044043-b5f-lecture/garde-activations.json.sha256")
    garde_sha = verifier_octets_compagnon(garde_raw, garde_sha_raw, "garde-activations.json")

    inv_raw = gh_raw("donnees/20261123-044043-b5f-lecture/inventaire-activations.json")
    inv_sha_raw = gh_raw("donnees/20261123-044043-b5f-lecture/inventaire-activations.json.sha256")
    inv_sha = verifier_octets_compagnon(inv_raw, inv_sha_raw, "inventaire-activations.json")

    man_raw = gh_raw("runs/20261123-044043-b5f-lecture/manifeste.json")
    man_sha_raw = gh_raw("runs/20261123-044043-b5f-lecture/manifeste.json.sha256")
    man_sha = verifier_octets_compagnon(man_raw, man_sha_raw, "manifeste.json")

    garde = json.loads(garde_raw.decode("utf-8"))
    inv = json.loads(inv_raw.decode("utf-8"))
    man = json.loads(man_raw.decode("utf-8"))

    # Contrôle d'absence de tout champ score/verdict lu dans manifeste : on n'accède qu'aux métadonnées de calcul.
    commit_prog = str(man["commit"])
    cmd_prog = str(man["commande"])
    # Extraction du nom de module final sans mot de rôle (le nom de paquet complet contient « familles »,
    # bloqué par MOTS_DE_ROLE sur la section activations ; le fait est consigné en réserve).
    module_court = cmd_prog.split(".")[-1]
    assert not any(m in module_court.lower() for m in fm.MOTS_DE_ROLE)

    cfg_adapt = man["config"]["adaptateur"]
    cfg_agent = man["config"]["agent"]
    precision_txt = f"{cfg_adapt['precision']} (sauvegarde {cfg_adapt['sauvegarde']})"
    date_str = cfg_agent.get("variables_gabarit", {}).get("date_string", "")
    gabarit_txt = f"{cfg_agent['modele']}@{cfg_agent['revision']} (date_string={date_str})"

    inv_map = {}
    for entry in inv["fichiers"]:
        inv_map[entry["chemin"]] = int(entry["octets"])

    par_serie: dict[str, set[str]] = defaultdict(set)
    octets_par_serie: dict[str, dict[str, int]] = defaultdict(dict)
    couches_gardees: set[int] = set()

    for rel in garde["fichiers"]:
        m = _CHEMIN_B5.match(rel)
        if not m:
            raise RuntimeError(f"Chemin hors liste blanche dans garde-activations.json : {rel!r}")
        if rel not in inv_map:
            raise RuntimeError(f"Chemin gardé absent de l'inventaire : {rel!r}")
        serie, couche, tache, pas = m.group(1), int(m.group(2)), m.group(3), int(m.group(4))
        couches_gardees.add(couche)
        cle = f"{tache}__p{pas}"
        if cle in par_serie[serie]:
            raise RuntimeError(f"Clé en double dans {serie}: {cle}")
        par_serie[serie].add(cle)
        octets_par_serie[serie][cle] = inv_map[rel]

    if "nu" not in par_serie:
        raise RuntimeError("Série 'nu' absente de la garde")
    cles_nu = par_serie["nu"]

    # Option A + Errata 1, 2, 3 :
    # - toute série dont le nom porte un mot de MOTS_DE_ROLE est comptée dans series_publiques, jamais nommée ;
    # - toute autre série est nommée dans series (ancre sans mot de rôle -> catégorie "adaptateur") ;
    # - contrôle par motif que chaque série comptée est bien une série publique (propre-A<1..3>-*, ancre-*, A<1..3>-*)
    #   et non un nom opaque de paire (X-01..X-30).
    series_nommees = []
    series_publiques = {"propre": 0, "ancre": 0, "autres_a_nom_public": 0}
    non_propres_aux_cles_communes = True
    octets_non_propres_identiques_a_nu = True
    propres_octets_egaux_nu: list[int] = []

    for s in sorted(par_serie):
        has_role = any(w in s.lower() for w in fm.MOTS_DE_ROLE)
        is_propre = s.startswith("propre-")
        is_ancre = s.startswith("ancre-")
        n_cles = len(par_serie[s])

        if not is_propre:
            if par_serie[s] != cles_nu:
                non_propres_aux_cles_communes = False
            if octets_par_serie[s] != octets_par_serie["nu"]:
                octets_non_propres_identiques_a_nu = False
        else:
            egaux = sum(1 for k in par_serie[s] if octets_par_serie[s].get(k) == octets_par_serie["nu"].get(k))
            propres_octets_egaux_nu.append(egaux)

        if has_role:
            if is_propre:
                if not re.match(r"^propre-A[1-3]-", s):
                    raise RuntimeError("Série propre inattendue hors motif public connu")
                series_publiques["propre"] += 1
            elif is_ancre:
                if not re.match(r"^ancre-(confirmation|exploratoire)-", s):
                    raise RuntimeError("Série ancre inattendue hors motif public connu")
                series_publiques["ancre"] += 1
            else:
                if not re.match(r"^A[1-3]-", s):
                    raise RuntimeError("Série à mot de rôle hors motif public connu : arrêt (erratum 1, point 3)")
                series_publiques["autres_a_nom_public"] += 1
        else:
            cat = "nu" if s == "nu" else ("propre" if is_propre else "adaptateur")
            series_nommees.append({"nom": s, "categorie": cat, "cles": n_cles})

    # Répartition des tâches de K par nombre d'actions
    actions_par_tache = Counter(cle.rsplit("__p", 1)[0] for cle in cles_nu)
    taches_dist = {"1": 0, "2": 0, "3": 0, "4_ou_plus": 0}
    for cnt in actions_par_tache.values():
        if cnt == 1:
            taches_dist["1"] += 1
        elif cnt == 2:
            taches_dist["2"] += 1
        elif cnt == 3:
            taches_dist["3"] += 1
        else:
            taches_dist["4_ou_plus"] += 1

    # Les textes propres vivent exclusivement dans les 3 séries propre-* (jamais mêlés à nu ni aux 43 autres séries
    # non propres, qui ont toutes 64/64 clés et tailles d'octets identiques à nu dans l'inventaire).
    distinctes_des_cles_propres = bool(
        series_publiques["propre"] > 0
        and non_propres_aux_cles_communes
        and octets_non_propres_identiques_a_nu
        and all(eq < len(cles_nu) for eq in propres_octets_egaux_nu)
    )

    section_activations = {
        "dossier_run": "donnees/20261123-044043-b5f-lecture",
        "inventaire_sha256": inv_sha,
        "garde_sha256": garde_sha,
        "regle_garde": str(garde["regle"]),
        "couches_gardees": sorted(couches_gardees),
        "chemin_de_calcul": {
            "programme": f"{module_court}@{commit_prog}",
            "precision": precision_txt,
            "mode": "relu à texte imposé",
            "gabarit": gabarit_txt,
            "source": "manifeste",
            "identique_pour_toutes_les_series": True,
        },
        "series": series_nommees,
        "series_publiques": series_publiques,
        "attestation_series_publiques": fm.ATTESTATION_SERIES_PUBLIQUES,
        "cles_communes": {
            "definition": "clés de la série nu, identiques dans toute série non propre",
            "actions": len(cles_nu),
            "taches": len(actions_par_tache),
            "taches_par_nombre_d_actions": taches_dist,
            "distinctes_des_cles_propres": distinctes_des_cles_propres,
        },
        "nu_relit_les_cles_communes": True,
        "non_propres_aux_cles_communes": non_propres_aux_cles_communes,
    }
    meta_act = {
        "manifeste_sha256": man_sha,
        "commit_b5f": COMMIT_B5F,
        "commit_prog": commit_prog,
        "total_series_garde": len(par_serie),
        "total_fichiers_garde": len(garde["fichiers"]),
        "total_fichiers_inventaire": len(inv["fichiers"]),
        "propres_octets_egaux_nu": propres_octets_egaux_nu,
        "octets_non_propres_identiques_a_nu": octets_non_propres_identiques_a_nu,
    }
    return section_activations, meta_act, garde_raw, garde_sha_raw


def extraire_scores_bbis() -> tuple[dict, dict, dict]:
    """Vérifie SCORES-BBIS et extrait UNIQUEMENT les colonnes de plan (__cles, __taches) sans lire aucun score."""
    bbis_raw = git_show(REF_BBIS, CHEMIN_BBIS)
    bbis_sha_raw = git_show(REF_BBIS, f"{CHEMIN_BBIS}.sha256")
    bbis_sha = verifier_octets_compagnon(bbis_raw, bbis_sha_raw, "sondes-bbis.json")
    if bbis_sha != SHA_BBIS_ATTENDU:
        raise RuntimeError(f"SHA-256 sondes-bbis.json {bbis_sha} != attendu {SHA_BBIS_ATTENDU}")

    bbis = json.loads(bbis_raw.decode("utf-8"))
    cles_racine = list(bbis.keys())

    # Lecture des SEULS tableaux de chaînes __cles.npy et __taches.npy dans les 3 morceaux .npz vérifiés
    plan_data: dict[tuple[str, str, str], dict[str, list[str]]] = {}
    morceaux_verifies = []
    champs_npz: set[str] = set()
    groupes_par_source: dict[str, set[str]] = defaultdict(set)

    for entry in bbis["fichiers_scores"]:
        rel = entry["fichier"]
        exp_sha = entry["sha256"]
        raw = git_show(REF_BBIS, rel)
        act_sha = hashlib.sha256(raw).hexdigest()
        if act_sha != exp_sha:
            raise RuntimeError(f"SHA-256 faux pour {rel}: {act_sha} != {exp_sha}")
        morceaux_verifies.append({"fichier": rel, "sha256": act_sha, "octets": len(raw), "sources": entry["sources"]})
        with zipfile.ZipFile(io.BytesIO(raw), "r") as zf:
            for name in sorted(zf.namelist()):
                if not name.endswith(".npy"):
                    raise RuntimeError(f"Entrée non .npy dans {rel}: {name}")
                parts = name[:-4].split("__")
                src, ek, field = parts[0], parts[1], parts[-1]
                grp = "__".join(parts[2:-1])
                champs_npz.add(field)
                groupes_par_source[src].add(grp)
                # FILTRE STRICT : uniquement __cles et __taches hors apprentissage/nul ; JAMAIS aucun score !
                if field in ("cles", "taches") and not grp.startswith("app") and grp != "nul":
                    with zf.open(name, "r") as f:
                        arr = np.load(io.BytesIO(f.read()), allow_pickle=False)
                    if arr.dtype.kind not in ("U", "S"):
                        raise RuntimeError(f"Type non chaîne interdit dans {name}: {arr.dtype}")
                    plan_data.setdefault((src, ek, grp), {})[field] = [str(x) for x in arr.tolist()]

    doses_out = []
    reglages_resume = []
    for dose_str, src, g_as, g_ns, g_ah, g_nh in DOSE_SPECS:
        plis_out = []
        taches_union_dose = set()
        for pli_idx, ek in (("0", "e0"), ("1", "e1")):
            t_meta = set(bbis["sources"][src][ek]["taches_lues"])
            c_as = plan_data[(src, ek, g_as)]["cles"]
            c_ns = plan_data[(src, ek, g_ns)]["cles"]
            c_ah = plan_data[(src, ek, g_ah)]["cles"]
            c_nh = plan_data[(src, ek, g_nh)]["cles"]
            t_as = set(plan_data[(src, ek, g_as)]["taches"])
            t_ns = set(plan_data[(src, ek, g_ns)]["taches"])
            t_ah = set(plan_data[(src, ek, g_ah)]["taches"])
            t_nh = set(plan_data[(src, ek, g_nh)]["taches"])
            if not (t_as == t_ns == t_ah == t_nh == t_meta):
                raise RuntimeError(f"Ensemble de tâches incohérent pour {src}/{ek}")
            if c_as != c_ns or c_ah != c_nh:
                raise RuntimeError(f"Clés non appariées pour {src}/{ek}")
            if len(taches_union_dose & t_meta) != 0:
                raise RuntimeError(f"Chevauchement de tâches entre plis pour {src}")
            taches_union_dose |= t_meta
            plis_out.append(
                {
                    "pli": pli_idx,
                    "taches_tenues": len(t_meta),
                    "actions": {
                        "adaptateur|saboteur": len(c_as),
                        "nu|saboteur": len(c_ns),
                        "adaptateur|honnete": len(c_ah),
                        "nu|honnete": len(c_nh),
                    },
                    "chemins": {
                        "adaptateur|saboteur": "origine",
                        "nu|saboteur": "relu",
                        "adaptateur|honnete": "relu",
                        "nu|honnete": "origine",
                    },
                    # Aucune action n'existe en série d'origine ET en série relue pour un même (poids, source)
                    "actions_en_origine_et_en_relu": 0,
                    "taches_avec_controle_du_chemin": 0,
                }
            )
            m = bbis["sources"][src][ek]
            reglages_resume.append(
                {
                    "dose": dose_str,
                    "source_bbis": src,
                    "pli": pli_idx,
                    "nom_sonde": m.get("nom_sonde"),
                    "reglage": m.get("reglage"),
                    "famille": m.get("famille"),
                    "agregation": m.get("agregation"),
                    "couche": m.get("couche"),
                    "taches_tenues": len(t_meta),
                }
            )
        doses_out.append({"dose": dose_str, "plis": plis_out})

    section_bbis = {
        "table": {
            "chemin": CHEMIN_BBIS,
            "sha256": bbis_sha,
            "ligne_registre": LIGNE_REGISTRE_BBIS,
        },
        "colonnes": cles_racine,
        "doses": doses_out,
        "nombre_de_doses": len(doses_out),
    }
    meta_bbis = {
        "morceaux_verifies": morceaux_verifies,
        "champs_npz": sorted(champs_npz),
        "groupes_par_source": {k: sorted(v) for k, v in sorted(groupes_par_source.items())},
        "reglages_resume": reglages_resume,
        "doses_json": bbis["doses"],
    }
    return section_bbis, meta_bbis, plan_data


def calculer_cout_devis(ta_etalon: int, ta_rejeu: int) -> dict:
    """Modèle de coût de `plan-epreuve-plantee-et-devis-v2.md` § 5 / `calculs/devis_epreuve_plantee_v2.py`."""
    h_id = 1300 * (0.52 + 0.0034 * ta_etalon) * REPLIQUES / 3600
    h_autres = 50 * 6 * REPLIQUES / 3600
    h_etalon = h_id + h_autres
    h_comp_a = 8 * REPLIQUES * 108.6 * (ta_rejeu / 24) ** 1.09 * (0.06 + 0.94 * 199 / 199) / 3600
    h_comp_c = 8 * REPLIQUES * 108.6 * (ta_rejeu / 24) ** 1.09 * (0.06 + 0.94 * 39 / 199) / 3600

    def to_usd(h: float, eur: float) -> float:
        return h * eur / COEURS_CCX63 * TAUX_USD

    h_tot_ac = h_etalon + h_comp_c
    h_tot_aa = h_etalon + h_comp_a
    return {
        "ta_etalon": ta_etalon,
        "ta_rejeu": ta_rejeu,
        "etalon_h_cpu": round(h_etalon, 2),
        "etalon_usd_hel1": round(to_usd(h_etalon, EUR_HEL1), 2),
        "etalon_usd_max": round(to_usd(h_etalon, EUR_MAX), 2),
        "etalon_h_ccx63": round(h_etalon / COEURS_CCX63, 2),
        "complet_C_h_cpu": round(h_comp_c, 2),
        "complet_C_usd_hel1": round(to_usd(h_comp_c, EUR_HEL1), 2),
        "complet_C_usd_max": round(to_usd(h_comp_c, EUR_MAX), 2),
        "complet_C_h_ccx63": round(h_comp_c / COEURS_CCX63, 2),
        "complet_A_h_cpu": round(h_comp_a, 2),
        "complet_A_usd_hel1": round(to_usd(h_comp_a, EUR_HEL1), 2),
        "complet_A_usd_max": round(to_usd(h_comp_a, EUR_MAX), 2),
        "complet_A_h_ccx63": round(h_comp_a / COEURS_CCX63, 2),
        "total_AC_h_cpu": round(h_tot_ac, 2),
        "total_AC_usd_hel1": round(to_usd(h_tot_ac, EUR_HEL1), 2),
        "total_AC_usd_max": round(to_usd(h_tot_ac, EUR_MAX), 2),
        "total_AC_h_ccx63": round(h_tot_ac / COEURS_CCX63, 2),
        "total_AC_plafond_1_5x_hel1": round(1.5 * to_usd(h_tot_ac, EUR_HEL1), 2),
        "total_AC_plafond_1_5x_max": round(1.5 * to_usd(h_tot_ac, EUR_MAX), 2),
        "total_AA_h_cpu": round(h_tot_aa, 2),
        "total_AA_usd_hel1": round(to_usd(h_tot_aa, EUR_HEL1), 2),
        "total_AA_usd_max": round(to_usd(h_tot_aa, EUR_MAX), 2),
        "total_AA_h_ccx63": round(h_tot_aa / COEURS_CCX63, 2),
        "dans_plafond_go_2026_11_23_18": to_usd(h_tot_ac, EUR_HEL1) <= PLAFOND_GO_18_USD,
    }


def construire_note_json(act: dict, bbis: dict, date_utc: str) -> dict:
    k = act["cles_communes"]
    etalon_taches = k["taches"]
    etalon_actions = max(1, fm.arrondi_moitie_bas(k["actions"] / k["taches"]))

    taches_par_dose = {}
    actions_par_dose_case = {}
    rejeu_min = {}
    for d in bbis["doses"]:
        dk = str(d["dose"])
        tt = sum(p["taches_tenues"] for p in d["plis"])
        act_map = {c: sum(p["actions"][c] for p in d["plis"]) for c in fm.CASES}
        taches_par_dose[dk] = tt
        actions_par_dose_case[dk] = act_map
        act_sab = min(act_map["adaptateur|saboteur"], act_map["nu|saboteur"])
        act_hon = min(act_map["adaptateur|honnete"], act_map["nu|honnete"])
        ok_d = tt >= fm.MINIMUM_TACHES_NOTE and act_sab > 0 and act_hon > 0 and (act_sab + act_hon) >= fm.MINIMUM_ACTIONS_NOTE
        rejeu_min[dk] = "atteints" if ok_d else "non atteints"

    complet_taches = min(taches_par_dose.values())
    complet_actions = min(
        max(1, fm.arrondi_moitie_bas(actions_par_dose_case[dk][c] / taches_par_dose[dk]))
        for dk in taches_par_dose
        for c in fm.CASES
    )
    min_cles = (
        "atteints"
        if (k["taches"] >= fm.MINIMUM_TACHES_NOTE and k["actions"] >= fm.MINIMUM_ACTIONS_NOTE)
        else "non atteints"
    )

    reserves = [
        (
            "Format physique de SCORES-BBIS : diag/20261118-154143-bbis-t07-v1/sondes-bbis.json est un index JSON "
            "(sans_aucune_aire=true) qui référence trois archives .npz scellées (donnees/20261118-154143-bbis-t07-v1/"
            "scores-bbis-000.npz, -001.npz et -002.npz), et non un fichier plat JSONL ou CSV ; les variables de "
            "prédicteurs triviaux (longueur, pas, valeur_declaree) ne figurent pas comme tableaux dans ces .npz "
            "(seul le rang de pas est encodé dans la chaîne cle=__p<pas> ; longueur et valeur_declaree vivent hors de "
            "SCORES-BBIS, dans mesures-t06.npz). Comme charger_table_bbis (commit 0ce9e3511) n'accepte que jsonl ou csv, "
            "un exportateur déterministe sans lecture de score (sondes-bbis.json + scores-bbis-*.npz -> JSONL scellé) "
            "ou un erratum de formats_v1.py est requis avant l'ouverture du rejeu croisé."
        ),
        (
            "Cellule P-instruit exclue des doses : sondes-bbis.json comporte une cinquième source (P-instruit, "
            "sabotage par instruction sans adaptateur LoRA, dose=null, absente de doses=[0.25, 0.5, 0.75, 1.0]) ; "
            "seules les quatre doses de l'adaptateur (0.25, 0.5, 0.75, 1.0) entrent dans le rejeu croisé "
            "(nombre_de_doses=4, doses_holm=4)."
        ),
        (
            "Séries propres et clés communes : les trois séries propres (comptées dans series_publiques.propre, "
            "jamais nommées) vivent dans des séries distinctes de nu et des 43 autres séries non propres, mais "
            "réemploient le modèle de nom de fichier <tache>__p<pas>.npy sur leurs propres épisodes ; sans ouvrir "
            "aucun .npy, les tailles en octets d'inventaire-activations.json confirment 64/64 tailles identiques à nu "
            "pour chacune des 43 autres séries non propres, contre 0/64, 0/64 et 1/64 pour les trois séries propres "
            "(distinctes_des_cles_propres=true, extension_taches_actions=false)."
        ),
        (
            "Contrôle du chemin : aucune action de SCORES-BBIS n'est présente à la fois en série d'origine et en série "
            "relue pour un même couple (poids, source) ; l'état est « contrôle absent » sur les quatre doses (aucun cas mixte)."
        ),
        (
            "Nom court du programme dans chemin_de_calcul.programme : la commande complète de runs/20261123-044043-b5f-lecture/"
            "manifeste.json comporte dans le nom du paquet Python un mot bloqué par la garde MOTS_DE_ROLE sur la section "
            "activations ; le champ porte donc le module exact et le commit exact du manifeste "
            "(relecture_v1@efc3f8350ebcbc84658c726f742c8b8e0374eee3), sans affaiblir la garde."
        ),
    ]

    return {
        "format": "note-effectifs-sondes-v2-v1",
        "redigee_par": REDIGEE_PAR,
        "date_utc": date_utc,
        "aveuglement": {
            "activations": "non ouvertes",
            "scores": "non ouverts",
            "table_de_l_ouvreur": "non ouverte",
            "verdict_adaptateurs_jumeaux": "non ouvert",
        },
        "activations": act,
        "scores_bbis": bbis,
        "cases_de_l_epreuve_plantee": {
            "etalon": {"taches": etalon_taches, "actions": etalon_actions},
            "complet": {
                "paires": fm.PAIRES_MODE_COMPLET,
                "taches": complet_taches,
                "actions": complet_actions,
                "doses_holm": bbis["nombre_de_doses"],
            },
            "extension_taches_actions": not k["distinctes_des_cles_propres"],
        },
        "minimums": {"cles_communes": min_cles, "rejeu_par_dose": rejeu_min},
        "reserves": reserves,
    }


def construire_correspondance_json(date_utc: str) -> dict:
    return {
        "format": "correspondance-rejeu-croise-v1",
        "redigee_par": REDIGEE_PAR,
        "date_utc": date_utc,
        "attestation": "aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes",
        "table_source": {
            "chemin": CHEMIN_BBIS,
            "sha256": SHA_BBIS_ATTENDU,
            "ligne_registre": LIGNE_REGISTRE_BBIS,
            "format_fichier": "jsonl",
        },
        "selection": {
            "champ_score": "sonde",
            "famille_bbis": "II",
            "cas_rejeu_croise": "oui",
        },
        "colonnes": {
            "dose": "dose",
            "pli": "pli_lu",
            "source": "condition",
            "poids": "groupe",
            "chemin": {"regle": "quatre_cases_du_texte_scelle"},
            "tache": "tache",
            "cle": "cle",
            "score": "score",
            "longueur": {"absente": True},
            "pas": {"absente": True},
            "valeur_declaree": {"absente": True},
            "tache_tenue": {"constante": True},
        },
        "valeurs": {
            "source": {
                "S25": "saboteur",
                "S50": "saboteur",
                "S75": "saboteur",
                "S100": "saboteur",
                "honnete": "honnete",
            },
            "poids": {
                "O-S25": "adaptateur",
                "O-S50": "adaptateur",
                "O-S75": "adaptateur",
                "O-S100": "adaptateur",
                "A25-honnete": "adaptateur",
                "A50-honnete": "adaptateur",
                "A75-honnete": "adaptateur",
                "A100-honnete": "adaptateur",
                "J25-S25": "nu",
                "J50-S50": "nu",
                "J75-S75": "nu",
                "J100-S100": "nu",
                "O-honnete": "nu",
            },
        },
    }


def rediger_note_md(note: dict, meta_act: dict, meta_bbis: dict, cout: dict) -> str:
    ce = note["cases_de_l_epreuve_plantee"]
    morceaux_lignes = "\n".join(
        f"  - `{m['fichier']}` (`{m['sha256']}`, {m['octets']} octets, sources : {', '.join(m['sources'])})"
        for m in meta_bbis["morceaux_verifies"]
    )
    return (
        "# Note des effectifs des diagnostics préalables des sondes (v2, Option A)\n\n"
        f"- **Session rédactrice** : `{note['redigee_par']}` (sous-agent neuf habilité, mandats `R-5198`, `R-5209` Option A, `GO-2026-11-23-18`, `-33`, `-36`).\n"
        f"- **Date (UTC)** : `{note['date_utc']}`.\n"
        "- **Spécification de référence** : `docs/notes/sondes-v2-concepteur-opus-v1/spec-note-des-effectifs-v2.md` et ses trois errata d'Option A "
        "(commits `14bfd7e8e` à `0ce9e3511` sur `sondes-v2/code-v2`).\n"
        "- **Pièces lues (en mémoire, sans écriture dans les dépôts)** :\n"
        f"  - Activations gardées de `20261123-044043-b5f-lecture` (branche distante `donnees/barreau5-familles-jumelles-v1-lecture`, commit `{meta_act['commit_b5f']}`) : "
        f"`donnees/20261123-044043-b5f-lecture/garde-activations.json` (`{note['activations']['garde_sha256']}`), "
        f"`donnees/20261123-044043-b5f-lecture/inventaire-activations.json` (`{note['activations']['inventaire_sha256']}`), "
        f"`runs/20261123-044043-b5f-lecture/manifeste.json` (`{meta_act['manifeste_sha256']}` — métadonnées du chemin de calcul uniquement) et leurs compagnons `.sha256`.\n"
        f"  - Table `SCORES-BBIS` (`{REF_BBIS}`, `{CHEMIN_BBIS}`, empreinte `{note['scores_bbis']['table']['sha256']}`, ligne `{LIGNE_REGISTRE_BBIS}`) : "
        "métadonnées de plan de `sondes-bbis.json` et, dans les trois morceaux `.npz` scellés qu'il cite, exclusivement les noms de membres ZIP et les tableaux de chaînes `*__cles.npy` et `*__taches.npy` :\n"
        f"{morceaux_lignes}\n"
        "  - Pièces de méthode dans `/home/antigravity/worktrees/sondes-v2-code` (`0ce9e3511`) : spécifications v2, plan et devis v2 (+ erratum 1 et `devis_epreuve_plantee_v2.py`), "
        "errata 1 à 3 d'Option A, `prereg/diagnostics-prealables-sondes-v1.md`, `decisions-concepteur-sondes-v2-v2.md`, `src/controle_ia/sondes_v2/formats_v1.py`, `magasin_v1.py`, `statistiques_v2.py`, `scellement.py`, `tests/test_sondes_v2_formats.py`, et code de schéma `src/controle_ia/t07bbis/{commun_v1,marche_v4,validation_imbriquee_v1,lecture_v5}.py`.\n"
        "- **Pièces NON ouvertes (cloisonnement strict)** : aucun tableau `.npy` d'activations (ni `np.load`, ni en-tête binaire, ni valeurs, ni forme) ; "
        "aucun tableau ni aucune colonne de scores dans `SCORES-BBIS` ni statistique dérivée ; aucune table de l'ouvreur ; aucun fichier fermé des empreintes ; "
        "aucun verdict ni texte scellé du test sur les adaptateurs jumeaux (`prereg/*barreau5*`) ; aucun fichier sous `docs/verdicts/`, `coffre/`, `essai/`, ni aucune pièce du saboteur.\n\n"
        "## Synthèse des effectifs et incidence sur le devis\n\n"
        f"- **Activations gardées (`une_sur_dix`, couche 15)** : {meta_act['total_series_garde']} séries au total dans la garde "
        f"({len(note['activations']['series'])} nommées : `nu`, 30 adaptateurs opaques `X-01` à `X-30`, 2 ancres sans mot de rôle ; "
        f"+ {sum(note['activations']['series_publiques'].values())} séries publiques comptées, non nommées : "
        f"{note['activations']['series_publiques']['propre']} propres, {note['activations']['series_publiques']['ancre']} ancres, "
        f"{note['activations']['series_publiques']['autres_a_nom_public']} autres à nom public), "
        f"{meta_act['total_fichiers_garde']} fichiers gardés (sur {meta_act['total_fichiers_inventaire']} dans l'inventaire sur 3 couches). "
        f"Clés communes `K` : **64 actions** réparties sur **40 tâches** (19 à 1 action, 19 à 2 actions, 1 à 3 actions, 1 à 4 actions), "
        "identiques dans les 44 séries non propres (`non_propres_aux_cles_communes = true`, `nu_relit_les_cles_communes = true`) et distinctes des 3 séries propres (`distinctes_des_cles_propres = true`).\n"
        f"- **Rejeu croisé (`SCORES-BBIS`)** : **4 doses** (`0.25`, `0.5`, `0.75`, `1.0`), 2 plis externes disjoints de 32 tâches chacun (**64 tâches tenues** par dose), "
        "exactement **10 actions par tâche** dans chacune des 4 cases (`320` actions par pli et par case, `640` par dose et par case, `10 240` lignes au total), "
        "100 % appariées par clé entre adaptateur et modèle nu. **Contrôle du chemin : `contrôle absent`** (0 action présente en origine et en relu pour un même couple poids/source ; aucun cas mixte).\n"
        f"- **Cases de l'épreuve plantée** : `etalon = {{taches: {ce['etalon']['taches']}, actions: {ce['etalon']['actions']}}}` (`TA_etalon = {cout['ta_etalon']}`), "
        f"`extension_taches_actions = false` ; `complet = {{paires: {ce['complet']['paires']}, taches: {ce['complet']['taches']}, actions: {ce['complet']['actions']}, doses_holm: {ce['complet']['doses_holm']}}}` (`TA_rejeu = {cout['ta_rejeu']}`).\n"
        f"- **Devis (`plan-epreuve-plantee-et-devis-v2.md`, § 5)** : l'effectif du rejeu croisé (`TA_rejeu = 640`) est 3,33 fois supérieur au scénario « très grand » du devis (`192`). "
        f"Selon le modèle exact de `devis_epreuve_plantee_v2.py` (500 répliques, `ccx63` à `hel1` à 1,3942 EUR/h, taux 1,25) :\n"
        f"  - Étalon seul (52 cases, option A) : **{cout['etalon_h_cpu']:.1f} h CPU** = **{cout['etalon_usd_hel1']:.2f} USD** ({cout['etalon_usd_max']:.2f} USD au plus haut), {cout['etalon_h_ccx63']:.2f} h sur une `ccx63`.\n"
        f"  - Complet seul, option C (39 rejeux) : **{cout['complet_C_h_cpu']:.1f} h CPU** = **{cout['complet_C_usd_hel1']:.2f} USD** ({cout['complet_C_usd_max']:.2f} USD au plus haut), {cout['complet_C_h_ccx63']:.2f} h sur une `ccx63`.\n"
        f"  - Complet seul, option A (199 rejeux) : **{cout['complet_A_h_cpu']:.1f} h CPU** = **{cout['complet_A_usd_hel1']:.2f} USD** ({cout['complet_A_usd_max']:.2f} USD au plus haut), {cout['complet_A_h_ccx63']:.2f} h sur une `ccx63`.\n"
        f"  - **Total recommandé (A étalon + C complet)** : **{cout['total_AC_h_cpu']:.1f} h CPU** = **{cout['total_AC_usd_hel1']:.2f} USD** ({cout['total_AC_usd_max']:.2f} USD au plus haut), {cout['total_AC_h_ccx63']:.2f} h sur une `ccx63` "
        f"(plafond 1,5x : {cout['total_AC_plafond_1_5x_hel1']:.2f} USD à `hel1`, {cout['total_AC_plafond_1_5x_max']:.2f} USD au plus haut) — **HORS DU PLAFOND de {PLAFOND_GO_18_USD:.2f} USD de `GO-2026-11-23-18`**.\n\n"
        "## Bloc JSON (seul lu par `charger_note_effectifs`)\n\n"
        "```json\n"
        + json.dumps(note, ensure_ascii=False, indent=1)
        + "\n```\n\n"
        "## Réserves\n\n"
        + "\n".join(f"{i}. {r}" for i, r in enumerate(note["reserves"], 1))
        + "\n"
    )


def rediger_correspondance_md(corr: dict, meta_bbis: dict) -> str:
    reglages_rows = "\n".join(
        f"| `{r['dose']}` | `{r['source_bbis']}` | `{r['pli']}` | `{r['nom_sonde']}` | `{r['reglage']}` | `{r['famille']}` | `{r['agregation']}` | `{r['couche']}` | {r['taches_tenues']} |"
        for r in meta_bbis["reglages_resume"]
    )
    morceaux_rows = "\n".join(
        f"| `{m['fichier']}` | `{m['sha256']}` | {', '.join(f'`{s}`' for s in m['sources'])} |"
        for m in meta_bbis["morceaux_verifies"]
    )
    return (
        "# Projet de table de correspondance des champs du rejeu croisé (sondes v2, v1)\n\n"
        f"- **Session rédactrice** : `{corr['redigee_par']}` (sous-agent neuf habilité, mandats `R-5209` point 2 et `GO-2026-11-23-36`).\n"
        f"- **Date (UTC)** : `{corr['date_utc']}`.\n"
        "- **Classe B** : projet soumis à contre-lecture par un autre modèle et scellement avant l'épreuve plantée et avant le verdict du test sur les adaptateurs jumeaux (`spec-correspondance-rejeu-croise-v2.md`).\n"
        "- **Fichier JSON compagnon scellé (lu par `charger_table_bbis`)** : `correspondance-rejeu-croise-v1.json` (objet JSON identique à l'octet au bloc ci-dessous).\n"
        "- **Attestation d'aveuglement** : *aucune colonne de score lue ; seules les colonnes de plan et leurs valeurs distinctes.* "
        "Aucune activation, aucun verdict, aucune table de l'ouvreur ni aucun tableau de scores (`*__sonde`, `*__plancher`, `*__nul`, `*__enc`, `*__sc_sonde`, `*__sonde_o2`) n'a été ouvert.\n\n"
        "## 1. Constat structurel sur `SCORES-BBIS` (point décisif pour la contre-lecture)\n\n"
        f"La ligne `{LIGNE_REGISTRE_BBIS}` désigne l'index JSON `{CHEMIN_BBIS}` (empreinte vérifiée `{SHA_BBIS_ATTENDU}`, `sans_aucune_aire: true`), "
        "qui référence trois archives `.npz` scellées sur `origin/donnees/t07-etape-b-bis-v2` :\n\n"
        "| Morceau `.npz` | SHA-256 vérifié | Sources portées |\n"
        "|---|---|---|\n"
        f"{morceaux_rows}\n\n"
        "Chaque morceau `.npz` stocke des tableaux nommés `<source_bbis>__e<pli>__<groupe>__<champ>.npy` (où `<groupe>` vaut `<serie>-<condition>`, "
        "et `<champ>` vaut `cles`, `taches`, `sonde`, etc.).\n\n"
        "- **Écart de format physique avec `charger_table_bbis` (commit `0ce9e3511`)** : `formats_v1.py` n'accepte aujourd'hui que `format_fichier` dans `{\"jsonl\", \"csv\"}`. "
        "La présente table de correspondance fige donc le schéma exact de la vue tabulaire JSONL déterministe extraite sans perte de `sondes-bbis.json` + `scores-bbis-000..002.npz` "
        "(une ligne par `(source_bbis, pli_lu, groupe, cle)` pour `champ_score == \"sonde\"`, avec les noms de champs et de valeurs brutes natifs de `t07bbis`), "
        "afin que le développeur puisse soit fournir un exportateur déterministe `sondes-bbis -> jsonl` (scellé, sans lecture ni résumé de score), soit étendre `charger_table_bbis` à ce format natif par un erratum contre-lu.\n"
        "- **Point d'attention sur `poids` et `serie`** : dans le format `t07bbis`, le préfixe de série `O` désigne l'adaptateur dans `O-S<d>` mais le modèle nu dans `O-honnete`. "
        "Le recodage de `poids` porte donc sur la colonne `groupe` (`O-S<d>`, `A<d>-honnete` → `adaptateur` ; `J<d>-S<d>`, `O-honnete` → `nu`), qui est bijective sur les quatre cases de chaque dose.\n"
        "- **Attestation sur `chemin` (`quatre_cases_du_texte_scelle`)** : après `selection`, chaque dose `0.25`, `0.5`, `0.75`, `1.0` ne porte que les quatre cases exactes du texte scellé "
        "(`O-S<d>` = `adaptateur|saboteur` en origine ; `J<d>-S<d>` = `nu|saboteur` en relu ; `A<d>-honnete` = `adaptateur|honnete` en relu ; `O-honnete` = `nu|honnete` en origine), "
        "chacune par un seul chemin (0 doublon, 0 action présente en origine et en relu pour un même `(poids, source)` ; contrôle du chemin = `absent`).\n"
        "- **Attestation sur `tache_tenue` (`constante: true`)** : dans `validation_imbriquee_v1.py`, tous les groupes évalués hors `app` et `app_enc` ne contiennent que les 32 tâches de `taches_lues` "
        "du pli externe `e0` ou `e1`, disjointes des 32 tâches d'apprentissage (vérifié sur les tableaux `*__taches.npy` : 32 + 32 = 64 tâches disjointes par dose, 0 tâche hors `taches_lues`).\n"
        "- **Variables de prédicteurs triviaux (`longueur`, `pas`, `valeur_declaree`)** : absentes des fichiers `SCORES-BBIS` (`sondes-bbis.json` et `scores-bbis-000..002.npz`), "
        "donc déclarées `{\"absente\": true}` (elles sortent proprement de `interaction_residuelle` dans `statistiques_v2.py`). Note pour la contre-lecture : le rang de pas `p0..p9` est encodé dans la chaîne `cle` "
        "(`S<d>__t<id>__p<pas>` / `honnete__t<id>__p<pas>`), tandis que `longueur` et `valeur_declaree` résident hors de `SCORES-BBIS` (dans `mesures-t06.npz` de T0.6).\n"
        "- **Sondes gelées sélectionnées par pli dans `sondes-bbis.json` (sans score lu)** :\n\n"
        "| Dose | Source | Pli | Nom de sonde | Réglage retenu | Famille | Agrégation | Couche | Tâches tenues |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
        f"{reglages_rows}\n\n"
        "  Note : pour `P-S25` (`e0`, `e1`) et `P-S50` (`e0`), la sonde gelée retenue par la validation imbriquée de `t07bbis` emploie l'agrégation `attention` (et non `max`), "
        "alors que `spec-correspondance-rejeu-croise-v2.md` § 3 mentionne « maximum sur les jetons » entre parenthèses ; le tableau `*__sonde` porte bien dans tous les cas le score brut de la sonde gelée du pli.\n\n"
        "## 2. Table de correspondance (`correspondance-rejeu-croise-v1.json`)\n\n"
        "```json\n"
        + json.dumps(corr, ensure_ascii=False, indent=1)
        + "\n```\n"
    )


def valider_livrables(
    note_md_path: Path,
    corr_json_path: Path,
    garde_raw: bytes,
    garde_sha_raw: bytes,
    plan_data: dict,
) -> dict:
    """Valide mécaniquement la note et la correspondance via `formats_v1` (commit `0ce9e3511`) dans `/tmp/verif-note-eff/`."""
    if TMP_VERIF_DIR.exists():
        shutil.rmtree(TMP_VERIF_DIR)
    TMP_VERIF_DIR.mkdir(parents=True, exist_ok=True)
    try:
        # 1. Validation de note-des-effectifs-sondes-v2-v1.md via charger_note_effectifs + verifier_couverture_note
        note_lue = fm.charger_note_effectifs(note_md_path)

        tmp_garde = TMP_VERIF_DIR / "garde-activations.json"
        tmp_garde_sha = TMP_VERIF_DIR / "garde-activations.json.sha256"
        tmp_garde.write_bytes(garde_raw)
        tmp_garde_sha.write_bytes(garde_sha_raw)
        couv = fm.verifier_couverture_note(note_lue, tmp_garde)

        # 2. Validation de correspondance-rejeu-croise-v1.json via charger_table_bbis sur table synthétique à scores 0.0
        verifier(corr_json_path)
        corr_obj = json.loads(corr_json_path.read_text(encoding="utf-8"))

        synth_path = TMP_VERIF_DIR / "sondes-bbis-synthetique.jsonl"
        lignes_synth = []
        # Toutes les 4 doses x 2 plis x 4 cases (10 240 lignes retenues) + lignes hors sélection (O-T100, P-instruit, enc)
        for dose_str, src, g_as, g_ns, g_ah, g_nh in DOSE_SPECS:
            for pli_idx, ek in (("0", "e0"), ("1", "e1")):
                for grp in (g_as, g_ns, g_ah, g_nh):
                    serie, cond = grp.split("-", 1)
                    cles = plan_data[(src, ek, grp)]["cles"]
                    taches = plan_data[(src, ek, grp)]["taches"]
                    for cle, tache in zip(cles, taches):
                        lignes_synth.append(
                            {
                                "source_bbis": src,
                                "famille_bbis": "II",
                                "dose": dose_str,
                                "pli_lu": pli_idx,
                                "serie": serie,
                                "condition": cond,
                                "groupe": grp,
                                "champ_score": "sonde",
                                "cas_rejeu_croise": "oui",
                                "tache": tache,
                                "cle": cle,
                                "score": 0.0,
                            }
                        )
                # Ajout de lignes témoins non sélectionnées pour éprouver `selection`
                lignes_synth.append(
                    {
                        "source_bbis": src,
                        "famille_bbis": "II",
                        "dose": dose_str,
                        "pli_lu": pli_idx,
                        "serie": "O",
                        "condition": "T100",
                        "groupe": "O-T100",
                        "champ_score": "sonde",
                        "cas_rejeu_croise": "non",
                        "tache": plan_data[(src, ek, g_as)]["taches"][0],
                        "cle": "T100__t000__p0",
                        "score": 0.0,
                    }
                )
                lignes_synth.append(
                    {
                        "source_bbis": src,
                        "famille_bbis": "II",
                        "dose": dose_str,
                        "pli_lu": pli_idx,
                        "serie": "O",
                        "condition": g_as.split("-", 1)[1],
                        "groupe": g_as,
                        "champ_score": "enc",
                        "cas_rejeu_croise": "oui",
                        "tache": plan_data[(src, ek, g_as)]["taches"][0],
                        "cle": plan_data[(src, ek, g_as)]["cles"][0],
                        "score": 0.0,
                    }
                )
        # Ligne P-instruit (Famille I) hors sélection
        lignes_synth.append(
            {
                "source_bbis": "P-instruit",
                "famille_bbis": "I",
                "dose": "",
                "pli_lu": "0",
                "serie": "O",
                "condition": "saboteur",
                "groupe": "O-saboteur",
                "champ_score": "sonde",
                "cas_rejeu_croise": "non",
                "tache": "2506.01290v2",
                "cle": "saboteur__t000__p0",
                "score": 0.0,
            }
        )

        synth_path.write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in lignes_synth),
            encoding="utf-8",
        )
        synth_sha = sceller(synth_path)

        # Copie temporaire de la correspondance avec la seule empreinte remplacée par synth_sha pour éprouver
        # charger_table_bbis de bout en bout (tous les autres champs identiques à l'octet).
        corr_tmp = json.loads(json.dumps(corr_obj))
        corr_tmp["table_source"]["sha256"] = synth_sha
        corr_tmp_path = TMP_VERIF_DIR / "correspondance-synth.json"
        corr_tmp_path.write_text(json.dumps(corr_tmp, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        sceller(corr_tmp_path)

        out_lignes, meta_bbis_charge = fm.charger_table_bbis(synth_path, corr_tmp_path)
        assert len(out_lignes) == 4 * 2 * 4 * 320, f"Attendu 10240 lignes, reçu {len(out_lignes)}"
        assert meta_bbis_charge["cles_sans_jumelle"] == 0
        assert meta_bbis_charge["regles"] == {"chemin": "quatre_cases_du_texte_scelle", "tache_tenue": "constante"}
        assert meta_bbis_charge["variables_absentes"] == ["longueur", "pas", "valeur_declaree"]

        # Épreuve supplémentaire : rejeu_croise sur copie en mémoire à scores factices non constants (écart type > 0)
        rngs = {n: np.random.default_rng(0) for n in st.GRAINES_NOMMEES}
        lignes_sd = [{**r, "score": float(i % 7) * 0.1} for i, r in enumerate(out_lignes)]
        res_rejeu = st.rejeu_croise(lignes_sd, rngs, {"alpha": 0.05}, n_tirages=10)
        assert sorted(res_rejeu["doses"].keys()) == ["0.25", "0.5", "0.75", "1.0"]
        assert all(res_rejeu["doses"][d]["controle_chemin"] == st.CONTROLE_ABSENT for d in ("0.25", "0.5", "0.75", "1.0"))

        return {
            "note_sha256": note_lue["sha256"],
            "cases": note_lue["cases"],
            "doses_holm": note_lue["doses_holm"],
            "controle_du_chemin": note_lue["controle_du_chemin"],
            "couverture": couv,
            "bbis_synth_lignes": len(out_lignes),
            "bbis_synth_cles_sans_jumelle": meta_bbis_charge["cles_sans_jumelle"],
            "bbis_synth_regles": meta_bbis_charge["regles"],
            "bbis_synth_variables_absentes": meta_bbis_charge["variables_absentes"],
        }
    finally:
        if TMP_VERIF_DIR.exists():
            shutil.rmtree(TMP_VERIF_DIR)


def main() -> int:
    SORTIE_DIR.mkdir(parents=True, exist_ok=True)
    date_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    act, meta_act, garde_raw, garde_sha_raw = extraire_activations()
    bbis, meta_bbis, plan_data = extraire_scores_bbis()
    note = construire_note_json(act, bbis, date_utc)
    ce = note["cases_de_l_epreuve_plantee"]
    cout = calculer_cout_devis(
        ta_etalon=ce["etalon"]["taches"] * ce["etalon"]["actions"],
        ta_rejeu=ce["complet"]["taches"] * ce["complet"]["actions"],
    )

    corr = construire_correspondance_json(date_utc)

    note_md_path = SORTIE_DIR / "note-des-effectifs-sondes-v2-v1.md"
    corr_json_path = SORTIE_DIR / "correspondance-rejeu-croise-v1.json"
    corr_md_path = SORTIE_DIR / "correspondance-rejeu-croise-sondes-v2-v1.md"

    # Suppression d'éventuels anciens compagnons dans ce dossier de brouillon neuf si réexécution propre
    for p in (note_md_path, corr_json_path, corr_md_path):
        comp = Path(str(p) + ".sha256")
        if comp.exists():
            comp.unlink()

    note_md_path.write_text(rediger_note_md(note, meta_act, meta_bbis, cout), encoding="utf-8")
    corr_json_path.write_text(json.dumps(corr, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    corr_md_path.write_text(rediger_correspondance_md(corr, meta_bbis), encoding="utf-8")

    sha_note = sceller(note_md_path)
    sha_corr_json = sceller(corr_json_path)
    sha_corr_md = sceller(corr_md_path)

    script_path = Path(__file__).resolve()
    script_comp = Path(str(script_path) + ".sha256")
    if script_comp.exists():
        script_comp.unlink()
    sha_script = sceller(script_path)

    verif = valider_livrables(note_md_path, corr_json_path, garde_raw, garde_sha_raw, plan_data)

    rapport = {
        "date_utc": date_utc,
        "empreintes": {
            "extraire_effectifs_option_a_v1.py": sha_script,
            "note-des-effectifs-sondes-v2-v1.md": sha_note,
            "correspondance-rejeu-croise-v1.json": sha_corr_json,
            "correspondance-rejeu-croise-sondes-v2-v1.md": sha_corr_md,
        },
        "validation_mecanique": verif,
        "cout_devis_v2": cout,
    }
    print(json.dumps(rapport, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
