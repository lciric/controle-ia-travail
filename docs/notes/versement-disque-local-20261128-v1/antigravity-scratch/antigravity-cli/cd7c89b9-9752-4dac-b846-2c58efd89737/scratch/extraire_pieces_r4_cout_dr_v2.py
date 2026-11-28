import hashlib
import json
import math
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(
    r"C:\Users\lciri\.gemini\antigravity-cli\brain"
    r"\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch"
)
VAST_EXE = SCRATCH / "venv-py314" / "Scripts" / "vastai.exe"
WT_DR = SCRATCH / "lecture-dr"
WT_B8 = SCRATCH / "wt-b8-puissance"
PAQUET = SCRATCH / "paquet-juge-r13-cout-dr"
sys.path.insert(0, str(WT_DR / "src"))

from controle_ia.manifeste import generateur
from controle_ia.premier_test_ia.statistiques import cout_lisible
from controle_ia.scellement import verifier
from controle_ia.t06.cout import cout_action
from controle_ia.dose_reponse.conditions_v1 import CONDITIONS, FACTEURS_ECRITS

# 0. Point sur l'instance Vast.ai 62647167 (sondes v2, 72 cœurs)
print("=== 0. ÉTAT VAST.AI 62647167 & SONDES V2 ===")
vk = Path.home() / ".config" / "vastai" / "vast_api_key"
vast_key = os.environ.get("VAST_API_KEY", "").strip() or vk.read_text("utf-8").strip()
req = urllib.request.Request(
    "https://console.vast.ai/api/v0/instances/",
    headers={"Authorization": f"Bearer {vast_key}", "Accept": "application/json"},
)
with urllib.request.urlopen(req, timeout=20) as resp:
    insts = json.loads(resp.read().decode("utf-8")).get("instances", [])
i64 = next((i for i in insts if str(i.get("id")) == "62647167"), None)
if i64:
    print(f"62647167: status={i64.get('actual_status')} | cpu={i64.get('cpu_util')}% | mem={i64.get('mem_usage')}Go")
    try:
        logs = subprocess.check_output(
            [str(VAST_EXE), "logs", "62647167"],
            env={**os.environ, "VAST_API_KEY": vast_key, "PYTHONUTF8": "1"},
            text=True, timeout=20, stderr=subprocess.STDOUT,
        )
        print("  dernières lignes:", " | ".join(logs.splitlines()[-4:]))
    except Exception:
        pass
else:
    print("62647167: ABSENTE (terminée et autodétruite !)")

ls_suite = subprocess.check_output(
    ["git", "-C", str(REPO), "ls-remote", "origin", "refs/heads/calcul/sondes-v2-epreuve-plantee-v4-suite"],
    text=True,
).strip()
print("Branche suite sondes v2:", ls_suite or "(calcul en cours)", flush=True)

# 1. Extraction scellée du dossier R4 pour le juge R13 de la dose-réponse
print("\n=== 1. EXTRACTION SCELLÉE DU DOSSIER R4 ===")
p_lect_json = WT_DR / "diag/20261126-082824-dose-reponse-lecture/lecture-cout-dose-reponse.json"
p_man_lect = WT_DR / "runs/20261126-082824-dose-reponse-lecture/manifeste.json"
p_man_course = WT_DR / "runs/20261125-093202-dose-reponse/manifeste.json"
p_ep_course = WT_DR / "diag/20261125-093202-dose-reponse/episodes-dose-reponse.json"

sha_lect = verifier(p_lect_json)
sha_man_lect = verifier(p_man_lect)
sha_man_course = verifier(p_man_course)
sha_ep_course = verifier(p_ep_course)

lect_doc = json.loads(p_lect_json.read_text("utf-8"))
man_lect = json.loads(p_man_lect.read_text("utf-8"))
man_course = json.loads(p_man_course.read_text("utf-8"))
ep_course = json.loads(p_ep_course.read_text("utf-8"))

echantillons_attendus = lect_doc["resultat"]["audit"]["echantillons_a_relire"]
conds_r4 = sorted(echantillons_attendus.keys())
conds_focus = conds_r4 + ["consigne_neutre"]

d_blocs = WT_DR / "donnees/20261125-093202-dose-reponse/blocs"
lignes_mesures = []
episodes_tous = []
textes_par_cle = {}
textes_par_quad = {}
textes_par_ep_pas = {}
empreintes_blocs = []

for bdir in sorted(d_blocs.glob("*")):
    sha_b = verifier(bdir / "bloc.json")
    empreintes_blocs.append(sha_b)
    corps_b = json.loads((bdir / "bloc.json").read_text("utf-8"))
    for f_nom, f_sha in corps_b["fichiers"].items():
        assert verifier(bdir / f_nom) == f_sha, f"Altération {bdir / f_nom}"
    for raw_l in (bdir / "mesures.jsonl").read_text("utf-8").splitlines():
        lignes_mesures.append(json.loads(raw_l))
    episodes_tous.extend(json.loads((bdir / "episodes.json").read_text("utf-8")))
    for raw_t in (bdir / "textes.jsonl").read_text("utf-8").splitlines():
        t_obj = json.loads(raw_t)
        if "cle" in t_obj:
            textes_par_cle[t_obj["cle"]] = t_obj
        if all(k in t_obj for k in ("condition", "tache", "replique", "pas")):
            textes_par_quad[(t_obj["condition"], t_obj["tache"], t_obj["replique"], t_obj["pas"])] = t_obj
        if all(k in t_obj for k in ("episode", "pas")):
            textes_par_ep_pas[(t_obj["episode"], t_obj["pas"])] = t_obj

entrees_sha = hashlib.sha256("".join(sorted(empreintes_blocs)).encode()).hexdigest()
assert entrees_sha == lect_doc["resultat"]["entrees_sha256"]

episodes_par_id = {e["episode"]: e for e in episodes_tous}
episodes_par_cr = {(e.get("condition"), e.get("tache"), e.get("replique")): e for e in episodes_tous}

synthese_injection_15_conditions = {}
for c in CONDITIONS:
    eps_c = [e for e in episodes_tous if e.get("condition") == c]
    injs = [e.get("injection") or {} for e in eps_c]
    consignes_sha = sorted({str(inj.get("consigne_sha256") or inj.get("sha256_consigne") or inj.get("empreinte_consigne") or "") for inj in injs})
    nb_pas_note = sorted({
        len(inj["pas_avec_note"]) if isinstance(inj.get("pas_avec_note"), list)
        else (len(e["pas_designes"]) if isinstance(e.get("pas_designes"), list) else -1)
        for e, inj in zip(eps_c, injs)
    })
    synthese_injection_15_conditions[c] = {
        "nb_episodes": len(eps_c),
        "tous_conformes": all(bool(inj.get("conforme")) for inj in injs),
        "cles_journal_injection": sorted({k for inj in injs for k in inj.keys()}),
        "consignes_sha256_distinctes": consignes_sha,
        "cardinalites_pas_designes_ou_note": nb_pas_note,
    }

graines_course = man_course.get("graines", {})
verif_permutations_pas = {"graines_presentes_manifeste_course": False, "couples_verifies": 0, "tous_concordants": True, "ecarts": []}
taches_triees = sorted({e["tache"] for e in episodes_tous})
if any(k.startswith("pas-designes/") for k in graines_course):
    verif_permutations_pas["graines_presentes_manifeste_course"] = True
    for t_id in taches_triees:
        for rep in (1, 2):
            g_key = f"pas-designes/{t_id}/{rep}"
            perm = [int(x) for x in generateur(graines_course[g_key]).permutation(10)]
            att_20, att_50 = sorted(perm[:2]), sorted(perm[:5])
            e20 = episodes_par_cr[("proportion_20_10", t_id, rep)]
            e50 = episodes_par_cr[("proportion_50_10", t_id, rep)]
            for ep_x, att_x, nom_c in ((e20, att_20, "proportion_20_10"), (e50, att_50, "proportion_50_10")):
                obs = ep_x.get("pas_designes")
                if obs is None and isinstance(ep_x.get("injection"), dict):
                    obs = ep_x["injection"].get("pas_avec_note") or ep_x["injection"].get("pas_designes")
                if obs is not None and sorted(int(z) for z in obs) != att_x:
                    verif_permutations_pas["tous_concordants"] = False
                    verif_permutations_pas["ecarts"].append({"condition": nom_c, "tache": t_id, "replique": rep, "attendu": att_x, "observe": obs})
            verif_permutations_pas["couples_verifies"] += 1

journaux_episodes_focus = {
    c: sorted([e for e in episodes_tous if e.get("condition") == c], key=lambda x: (x.get("tache", ""), x.get("replique", 0)))
    for c in conds_focus
}

comptes_detailles_par_condition = {}
for c in CONDITIONS:
    L = [l for l in lignes_mesures if l["condition"] == c]
    lis = [l for l in L if cout_lisible(l["cout"])]
    illis = [l for l in L if not cout_lisible(l["cout"])]
    comptes_detailles_par_condition[c] = {
        "episodes": sum(1 for e in episodes_tous if e.get("condition") == c),
        "actions": len(L),
        "actions_valides": sum(bool(l.get("valide", True)) for l in L),
        "actions_pas_designe": sum(bool(l.get("designe")) for l in L),
        "lisibles": len(lis),
        "illisibles_total": len(illis),
        "cout_none": sum(l["cout"] is None for l in L),
        "cout_non_positif_ou_non_fini": sum(l["cout"] is not None and not cout_lisible(l["cout"]) for l in L),
        "tronquees_400_jetons": sum(bool(l.get("tronquee")) for l in L),
        "nb_cout_present": sum(bool(l.get("cout_present")) for l in L) if any("cout_present" in l for l in L) else None,
        "par_forme_sur_lisibles": {
            "cout_multiplication": sum(bool(l["cout_multiplication"]) for l in lis),
            "cout_plusieurs_nombres": sum(bool(l["cout_plusieurs_nombres"]) for l in lis),
            "union_multiplication_ou_plusieurs_nombres": sum(bool(l["cout_multiplication"] or l["cout_plusieurs_nombres"]) for l in lis),
            "part_union_multiplication_ou_plusieurs_nombres": (
                sum(bool(l["cout_multiplication"] or l["cout_plusieurs_nombres"]) for l in lis) / len(lis) if lis else None
            ),
            "cout_intervalle": sum(bool(l["cout_intervalle"]) for l in lis),
            "cout_suffixe_k": sum(bool(l["cout_suffixe_k"]) for l in lis),
            "cout_milliers_espace": sum(bool(l["cout_milliers_espace"]) for l in lis),
        },
        "nb_cout_egal_facteur_sur_lisibles": {str(f): sum(abs(l["cout"] - f) <= 1e-9 for l in lis) for f in FACTEURS_ECRITS},
        "part_cout_egal_facteur_sur_lisibles": {
            str(f): (sum(abs(l["cout"] - f) <= 1e-9 for l in lis) / len(lis) if lis else None) for f in FACTEURS_ECRITS
        },
    }

verif_graines_r4 = {}
for c in conds_r4:
    cles_c = sorted(l["cle"] for l in lignes_mesures if l["condition"] == c)
    g_info = man_lect["graines"][f"audit-r4/{c}"]
    rng = generateur(g_info)
    tirees = sorted(cles_c[int(i)] for i in rng.choice(len(cles_c), size=min(20, len(cles_c)), replace=False))
    assert tirees == echantillons_attendus[c], f"Discordance graine R4 sur {c}"
    verif_graines_r4[c] = {
        "graine_manifeste": g_info,
        "nb_actions_condition": len(cles_c),
        "tirage_recalcule_egal_attendu": True,
        "cles_tirees": tirees,
    }

mesures_par_cle = {l["cle"]: l for l in lignes_mesures}
actions_60 = {c: [] for c in conds_r4}
nb_recalcul_cout_exact = 0
nb_actions_extraites = 0

for c in conds_r4:
    for cle_a in echantillons_attendus[c]:
        m_a = mesures_par_cle[cle_a]
        t_a = (
            textes_par_cle.get(cle_a)
            or textes_par_quad.get((m_a["condition"], m_a["tache"], m_a["replique"], m_a["pas"]))
            or textes_par_ep_pas.get((m_a.get("episode"), m_a["pas"]))
        )
        assert t_a is not None, f"Texte introuvable pour {cle_a}"
        texte_brut = next(
            (t_a[k] for k in ("texte", "action", "sortie", "contenu", "reponse") if isinstance(t_a.get(k), str)),
            None,
        )
        assert isinstance(texte_brut, str)
        res_ca = cout_action(texte_brut)
        if isinstance(res_ca, dict):
            val_ca = next((res_ca[k] for k in ("cout", "valeur", "cost") if k in res_ca), None)
        else:
            val_ca = res_ca

        c_mes = m_a["cout"]
        if val_ca is None and c_mes is None:
            egal_cout = True
        elif isinstance(val_ca, (int, float)) and isinstance(c_mes, (int, float)):
            if math.isnan(val_ca) and math.isnan(c_mes):
                egal_cout = True
            elif math.isfinite(val_ca) and math.isfinite(c_mes):
                egal_cout = abs(float(val_ca) - float(c_mes)) <= 1e-12
            else:
                egal_cout = (val_ca == c_mes)
        else:
            egal_cout = (val_ca == c_mes)

        if egal_cout:
            nb_recalcul_cout_exact += 1
        lignes_cost = [ln for ln in texte_brut.splitlines() if "cost" in ln.lower()]
        ep_a = episodes_par_id.get(m_a.get("episode")) or episodes_par_cr.get((m_a["condition"], m_a["tache"], m_a["replique"]))
        actions_60[c].append({
            "cle": cle_a,
            "mesures": m_a,
            "verification_cout_action_recalcule": {
                "cout_mesures_jsonl": c_mes,
                "sortie_complete_t06_cout_action": res_ca,
                "valeur_extraite": val_ca,
                "concordant": egal_cout,
                "lignes_contenant_cost": lignes_cost,
            },
            "fiche_texte_jsonl": t_a,
            "fiche_episode_et_injection": ep_a,
        })
        nb_actions_extraites += 1

dossier_r4 = {
    "objet": "Pièces de relecture préalable de l'audit de symétrie R4 (section Seuil de prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md)",
    "sources_scellees": {
        "prereg_sha256": "2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41",
        "run_course": "20261125-093202-dose-reponse",
        "manifeste_course_sha256": sha_man_course,
        "episodes_dose_reponse_sha256": sha_ep_course,
        "entrees_64_blocs_sha256": entrees_sha,
        "run_lecture": "20261126-082824-dose-reponse-lecture",
        "manifeste_lecture_sha256": sha_man_lect,
        "lecture_cout_dose_reponse_sha256": sha_lect,
    },
    "resume_course_hors_couts": ep_course.get("resultat", {}),
    "piece_1_journaux_injection": {
        "synthese_15_conditions": synthese_injection_15_conditions,
        "verification_permutations_pas_designes": verif_permutations_pas,
        "journaux_complets_episodes_conditions_concernees_et_neutre": journaux_episodes_focus,
    },
    "piece_2_comptes_detailles_et_graines_r4": {
        "comptes_par_condition_15": comptes_detailles_par_condition,
        "verification_graines_audit_r4": verif_graines_r4,
    },
    "piece_3_echantillons_60_actions_tirees_par_graine": actions_60,
}

PAQUET.mkdir(parents=True, exist_ok=True)
out_p = PAQUET / "pieces-relecture-r4-cout-dose-reponse-v1.json"
raw_out = (json.dumps(dossier_r4, ensure_ascii=False, indent=2, default=str) + "\n").encode("utf-8")
out_p.write_bytes(raw_out)
sha_out = hashlib.sha256(raw_out).hexdigest()
(PAQUET / "pieces-relecture-r4-cout-dose-reponse-v1.json.sha256").write_bytes(
    f"{sha_out}  pieces-relecture-r4-cout-dose-reponse-v1.json\n".encode("utf-8")
)

st_dr = subprocess.check_output(["git", "-C", str(WT_DR), "status", "--porcelain"], text=True).strip()
assert st_dr == "", f"lecture-dr sale: {st_dr}"
print(f"PIECES_R4_PRETES_OK: {out_p} ({len(raw_out)} octets)")
print(f"SHA256_PIECES_R4: {sha_out}")
print(f"VERIF_60_ACTIONS: extraits={nb_actions_extraites}/60 | cout_concordant={nb_recalcul_cout_exact}/60 | graines_r4_ok=True | permutations_pas_ok={verif_permutations_pas['tous_concordants']}")

# 2. Afficher mandat-juge-lecture-sondes-barreau8-v3.md (lecture seule, zéro ouverture de lecture-sondes-barreau8-v1.json)
print("\n=== 2. CONTENU DE mandat-juge-lecture-sondes-barreau8-v3.md ===")
p_mj = WT_B8 / "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-juge-lecture-sondes-barreau8-v3.md"
print(p_mj.read_text("utf-8"))
