import hashlib
import json
import pathlib
import subprocess
import sys
import types
import os

REPO = pathlib.Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
sys.path.insert(0, str(REPO / "src"))

# Pure-stdlib stub for heavy ML deps ONLY so we can import the unmodified lecture_sondes_v6.py
# in sandboxed Python 3.14 (exiger_attestation_course uses 0 ML deps).
for mod_name in ("numpy", "scipy", "scipy.stats", "torch", "torch.nn", "sklearn", "sklearn.metrics", "sklearn.linear_model"):
    if mod_name not in sys.modules:
        m = types.ModuleType(mod_name)
        if mod_name == "numpy":
            m.ndarray = object
            m.float64 = float
            m.float32 = float
            m.int64 = int
            m.uint8 = int
        if mod_name == "scipy.stats":
            m.norm = object
            m.rankdata = object
        if mod_name == "torch":
            m.Tensor = object
        sys.modules[mod_name] = m

from controle_ia import scellement
from controle_ia.barreau8_moniteurs import lecture_sondes_v6 as ls6

d15 = {
    "avertissement": "EXPLORATOIRE, NON OPPOSABLE (R-522) : attestation de la course et de l'oracle, sans contenu, pour le côté moniteurs",
    "commit_lancement": "192a429e67b93e9a89d273ba5a4b5c0c61d139f1",
    "lancements": {
        "nombre": 1,
        "premier_acheve": "oui",
        "rang_du_lancement_lu": 1,
    },
    "ligne_de_calcul": "GO-2026-11-22-75",
    "oracle": {
        "designation": {
            "heure": "2026-11-23T04:05:15Z",
            "sha256": "78045af708e521474d75693b314dc2b4b9a68134c14813722b53eb14825253d6",
        },
        "designation_avant_la_premiere_sortie_de_l_evaluation": "oui",
        "designe_par_la_regle": "oui",
        "lectures_jouees_sous_cet_oracle": "oui",
        "regle": "c1dc54597a1ab4b467331673607d986e46a706c06253bb40070e5d15caaa61f2",
        "regle_scellee_avant_la_premiere_sortie": "oui",
    },
    "ordre_du_lancement": {
        "egal_a_l_ordre_neuf": "oui",
        "sha256": "8e1d340a2e676b722489e6ae68b6ed9cd7d96bcf95d42e3490557ab3db7fb6c9",
    },
    "premieres_sorties": {
        "course": "2026-11-23T04:41:59Z",
        "etalonnage": "2026-11-22T20:29:04Z",
        "evaluation": "2026-11-23T11:24:13Z",
    },
    "run_id": "20261123-043944-iib-course-reel",
    "verdict_mecanique": "conforme",
}

stage_root = pathlib.Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\5e23ba2b-b020-412c-9e05-9991f87a0eae\scratch\d15-stage")
dest = stage_root / ls6.Pieces().attestation_course
dest.parent.mkdir(parents=True, exist_ok=True)

json_text = json.dumps(d15, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
json_bytes = json_text.encode("utf-8")
assert b"\r" not in json_bytes, "CR found in JSON!"
dest.write_bytes(json_bytes)

sha_json = hashlib.sha256(json_bytes).hexdigest()
sha_text = f"{sha_json}  {dest.name}\n"
sha_bytes = sha_text.encode("utf-8")
assert b"\r" not in sha_bytes, "CR found in .sha256!"
sha_path = dest.with_name(dest.name + ".sha256")
sha_path.write_bytes(sha_bytes)
sha_of_sha = hashlib.sha256(sha_bytes).hexdigest()

# 1. Verify seal via controle_ia.scellement.verifier
ver = scellement.verifier(dest)
assert ver == sha_json, f"scellement.verifier mismatch: {ver} != {sha_json}"

# 2. Verify run_id against etats-lectures-iib-v1.json (30cf3b57 AND main) and D-13
env = {"GIT_TERMINAL_PROMPT": "0", "PATH": os.environ.get("PATH", "")}
etats_30cf = json.loads(subprocess.check_output(
    ["git", f"--git-dir={REPO / '.git'}", "show", "30cf3b578f8b9c748fddfc87c4b6e7dd0a506abf:docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json"],
    env=env,
).decode("utf-8"))
etats_main = json.loads((REPO / "docs/notes/barreau8-cote-moniteurs-entrees-v1/etats-lectures-iib-v1.json").read_text(encoding="utf-8"))
d13 = json.loads((REPO / "docs/notes/rejeu-activations-saboteur-voie-a-v1/prealables-cote-expose-v7-brouillon/extrait-cote-expose-d13-v1.json").read_text(encoding="utf-8"))
assert d15["run_id"] == etats_30cf["run_id"] == etats_main["run_id"] == d13["run_id"]
assert d15["commit_lancement"] == d13["commit_lancement"]

# 3. Verify via unmodified lecture_sondes_v6.exiger_attestation_course (healthy case)
mandat_simule = f"Mandat lecteur citant D-15 : {sha_json}\n"
res = ls6.exiger_attestation_course(
    racine=stage_root,
    pieces=ls6.Pieces(),
    texte_du_mandat_du_lecteur=mandat_simule,
    run_id_etats=etats_30cf["run_id"],
    run_id_trace=d13["run_id"],
)

# 4. Negative artefact checks (R5): wrong run_id and missing sha in mandat must raise Refus("22")
for label, kw in [
    ("wrong_run_id", dict(racine=stage_root, pieces=ls6.Pieces(), texte_du_mandat_du_lecteur=mandat_simule, run_id_etats="autre-run", run_id_trace=d13["run_id"])),
    ("missing_sha_in_mandat", dict(racine=stage_root, pieces=ls6.Pieces(), texte_du_mandat_du_lecteur="sans empreinte", run_id_etats=etats_30cf["run_id"], run_id_trace=d13["run_id"])),
]:
    try:
        ls6.exiger_attestation_course(**kw)
        raise AssertionError(f"Expected Refus for {label}")
    except ls6.Refus as e:
        assert e.code == "22", f"Unexpected code {e.code} for {label}"
        print(f"ARTEFACT {label}: REFUS [22] OK ({e})")

# 5. Zero forbidden content check (no paths in oracle.regle/designation, exactly 9 top-level keys)
assert len(d15) == 9
assert "/" not in d15["oracle"]["regle"] and "\\" not in d15["oracle"]["regle"]
assert "/" not in d15["oracle"]["designation"]["sha256"]

print("VALIDATION exiger_attestation_course: PASS")
print("VALIDATION scellement.verifier: PASS")
print("Result:", json.dumps(res, indent=2, ensure_ascii=False))
print("JSON bytes:", len(json_bytes))
print("JSON sha256:", sha_json)
print("SHA256 file bytes:", len(sha_bytes))
print("SHA256 file sha256:", sha_of_sha)
print("SHA256 file content:", repr(sha_text))
print("--- EXACT JSON CONTENT ---")
print(json_text, end="")
