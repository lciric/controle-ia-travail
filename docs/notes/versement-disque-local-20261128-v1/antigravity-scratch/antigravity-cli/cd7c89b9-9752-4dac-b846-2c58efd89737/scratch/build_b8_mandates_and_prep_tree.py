"""Turnkey Barreau 8 post-D-10 script:
1. Verify & stage D-10 output (aires-minimales-detectables-barreau8-v1.json + manifeste)
2. Fill & seal reader mandate (v3) and judge mandate (v3, with R-5344 head reserve)
3. Validate ALL lecture_sondes_v6 guards (exiger_mandats, exiger_attestation_ordre, exiger_attestation_course, exiger_accord)
4. Commit & push D-10 + mandates + decisions entry to origin/main via fast sparse worktree
5. Prepare the clean detached reading tree (scratch/b8-lecture-arbre) with LIVRAISON-PASSE-IIB + D-8 probes, git status empty!
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT_PUISS = SCRATCH / "wt-b8-puissance"
WT_PUSH = SCRATCH / "wt-main-push"
STAGE = SCRATCH / "b8-staging"
COND = STAGE / "conductrice"
D8_SRC = STAGE / "donnees" / "20261114-001352-t07-lecture-reel"
ARBRE = SCRATCH / "b8-lecture-arbre"
PY_WIN = str(SCRATCH / "venv-py314" / "Scripts" / "python.exe").replace("\\", "/")
ARBRE_STR = str(ARBRE).replace("\\", "/")

env = os.environ.copy()
env["GIT_TERMINAL_PROMPT"] = "0"
_gh_tok = subprocess.check_output(["gh", "auth", "token"], text=True, timeout=25).strip()
env["_MEM_GH_TOK"] = _gh_tok
_askpass = SCRATCH / "_git_askpass_mem.cmd"
_askpass.write_text("@echo off\r\necho %_MEM_GH_TOK%\r\n", encoding="ascii")
env["GIT_ASKPASS"] = str(_askpass)

def git_run(cwd, *args, check=True, timeout=300, binary=False):
    p = subprocess.run(
        ["git", "-C", str(cwd), "-c", "credential.helper=",
         "-c", "core.longpaths=true", "-c", "core.protectNTFS=false", *args],
        env=env, capture_output=True, text=not binary, timeout=timeout,
    )
    if check and p.returncode != 0:
        err = p.stderr if not binary else p.stderr.decode("utf-8", errors="replace")
        err = err.replace(_gh_tok, "***")
        raise RuntimeError(f"git {args} failed rc={p.returncode}: {err[:400]}")
    return p

sys.path.insert(0, str(REPO / "src"))
from controle_ia import scellement
from controle_ia.barreau8_moniteurs import lecture_sondes_v6 as ls

RUN_ID_PUISS = "20261125-083300-puissance-barreau8"
REL_AIRES = f"diag/{RUN_ID_PUISS}/aires-minimales-detectables-barreau8-v1.json"
REL_MANIF = f"runs/{RUN_ID_PUISS}/manifeste.json"

src_aires = WT_PUISS / REL_AIRES
src_aires_sha = WT_PUISS / (REL_AIRES + ".sha256")
src_manif = WT_PUISS / REL_MANIF
src_manif_sha = WT_PUISS / (REL_MANIF + ".sha256")

assert src_aires.is_file() and src_aires_sha.is_file(), f"D-10 output not ready yet: {src_aires}"
assert src_manif.is_file() and src_manif_sha.is_file(), f"D-10 manifeste missing: {src_manif}"

sha_aires = scellement.verifier(src_aires)
sha_manif = scellement.verifier(src_manif)
print(f"D10_VERIFIED: aires={sha_aires} manif={sha_manif}")

# 1. Refresh fast sparse worktree WT_PUSH from origin/main
git_run(REPO, "fetch", "origin", "main")
if WT_PUSH.exists():
    git_run(REPO, "worktree", "remove", "--force", str(WT_PUSH), check=False)
    if WT_PUSH.exists():
        shutil.rmtree(WT_PUSH, ignore_errors=True)
git_run(REPO, "worktree", "add", "--no-checkout", "--detach", str(WT_PUSH), "origin/main")
git_run(WT_PUSH, "sparse-checkout", "init", "--cone")
git_run(WT_PUSH, "sparse-checkout", "set",
        "registres",
        "prereg",
        "docs/notes/code-lecture-sondes-v6-v1",
        "docs/notes/barreau8-cote-moniteurs-entrees-v1",
        "docs/notes/barreau8-cote-moniteurs-sorties-v1",
        "docs/notes/barreau8-cote-expose-pieces-lecture-v1",
        "docs/notes/barreau8-conductrice-lecture-sondes-v1")
git_run(WT_PUSH, "checkout")

# Copy D-10 files into WT_PUSH
for src, rel in (
    (src_aires, REL_AIRES),
    (src_aires_sha, REL_AIRES + ".sha256"),
    (src_manif, REL_MANIF),
    (src_manif_sha, REL_MANIF + ".sha256"),
):
    dst = WT_PUSH / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_bytes(src.read_bytes())

# 2. Fill & seal reader mandate first, then judge mandate (with R-5344 head reserve)
REL_MAND_LECTEUR = "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-lecteur-sondes-barreau8-v3.md"
REL_MAND_JUGE = "docs/notes/barreau8-conductrice-lecture-sondes-v1/mandat-juge-lecture-sondes-barreau8-v3.md"

EXCLUS_PATH = "docs/notes/barreau8-cote-expose-pieces-lecture-v1/liste-exclus-ordre-course-lue-v2.md"
EXCLUS_SHA = "43b9d4e1fe903509326b7501406c2b3233f8e5b762f44b7bf1d083ddc2e0c3e0"
QLQ_PATH = "registres/qui-a-lu-quoi-v23.md"
QLQ_SHA = "325ba2dd760afb607fc064f669807f93eb967dea2759f4de33b9b324b7e03e7a"
D15_SHA = "8ed8a6a9bd041e0ca63a2ac58000e44d7f8f4b73cdbcebfe70467ac06f01e595"
ETATS_SHA = "7329f08be94adda1ae0e5f44ea9d9b80dd7f614310343b39a39e87d1abab9e0c"
ATTEST_HORS = (
    f"l'agent désigné est lancé neuf, sans contexte hérité ; le rôle qu'il tient ne figure pas sur la liste à la section 1:8 "
    f"(contrôle de la session mère sur l'extrait scellé {EXCLUS_SHA} et le registre {QLQ_PATH} {QLQ_SHA}) ; "
    f"aucune pièce interdite ne lui est donnée"
)

def strip_work_header(text: str) -> str:
    idx = text.index("\n---\n")
    return text[idx + len("\n---\n"):].lstrip("\n")

def adapt_env(text: str) -> str:
    return (
        text.replace("/home/user/controle-ia-travail", ARBRE_STR)
            .replace(".venv/bin/python", PY_WIN)
    )

# Reader mandate
lect_raw = (COND / "projet-mandat-lecteur-sondes-v3-brouillon3.md").read_text(encoding="utf-8")
lect = strip_work_header(lect_raw)
lect_reps = {
    "<DESIGNATION_LECTEUR>": "agent neuf, modèle Gemini 4 Neon (autorisé sur le chemin critique de l'entretien du 1er décembre par GO-2026-11-24-49), lancé par la session mère après le versement de ce mandat, avec ce seul mandat pour consigne",
    "<CHEMIN_LISTE_EXCLUS>": EXCLUS_PATH,
    "<EMPREINTE_LISTE_EXCLUS>": EXCLUS_SHA,
    "<CHEMIN_QUI_A_LU_QUOI>": QLQ_PATH,
    "<EMPREINTE_QUI_A_LU_QUOI>": QLQ_SHA,
    "<ATTESTATION_HORS_EXCLUS>": ATTEST_HORS,
    "<EMPREINTE_ATTESTATION_COURSE>": D15_SHA,
    "<REFERENCE_BOITE_NOIRE ou « absente »>": "absente",
    "<HEURE_REMISE_NOTE_V7>": "2026-11-24T10:18:40Z",
    "<SOURCE>": "champ AD2-3 de l'additif 2 scellé (prereg/lecture-sondes-barreau8-v1-addendum-2-format-entrees-v1.md, ligne 153, commit 776eb628)",
    "<CHEMIN_BORDEREAU_CODE>": "docs/notes/code-lecture-sondes-v6-v1/bordereau-code-lecture-sondes-barreau8-v6.json",
    "<EMPREINTE_BORDEREAU_CODE>": "dd816daf261fbf6d261a21164fbe475391276795b761e28a7a1e8ec95e0e2d4e",
    "<IDENTIFIANT_ACCORD_LECTURE>": "GO-2026-11-24-28",
    "<ENTROPIE_F3>": "149333987590752343984325077404464904184",
    "<CHEMIN_SONDES_LEGERES>": "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz",
    "<CHEMIN_PLANCHERS>": "donnees/20261114-001352-t07-lecture-reel/planchers-figees-t07.npz",
    "<CHEMIN_SONDES_NEUVES>": "donnees/20261114-001352-t07-lecture-reel/sondes-neuves-t07.npz",
    "<CHEMIN_AIRES_MINIMALES>": REL_AIRES,
    "<EMPREINTE_AIRES_MINIMALES>": sha_aires,
    "<CHEMIN_MANDAT_LECTEUR>": REL_MAND_LECTEUR,
    "<CHEMIN_MANDAT_JUGE>": REL_MAND_JUGE,
    "<RECEPTION_DEJA_JOUEE>": "oui (jouée le 2026-11-24T15:50:30Z par la conductrice session_01Qi7Gr6acCdYGKsotBtUNvE, GARDE DE RÉCEPTION TENUE r1 à r7, bordereau 85bae5dcd9799f0a517f70eef2eb0d2c147ff3a3963fcb54f494e214a5a972fa ; sortie sur branche orpheline reception/barreau8-sortie-garde-v1 commit 274aac053f570571c20c20c1fe9c1c9acc4dae7e, empreinte abf70d27ba49bf450056c84105ffbf5eee053a2c76757b0f01a579023f8fcf95)",
    "<DOSSIER_JOURNAL>": str(SCRATCH / "journal-lecture-sondes-barreau8-v1").replace("\\", "/"),
}
for k, v in lect_reps.items():
    lect = lect.replace(k, v)
lect = adapt_env(lect).replace("\r\n", "\n")
leftover_l = re.findall(r"<[A-Z][A-Z0-9_]*", lect)
assert not leftover_l, f"Leftover placeholders in reader mandate: {leftover_l}"
p_lect = WT_PUSH / REL_MAND_LECTEUR
p_lect.parent.mkdir(parents=True, exist_ok=True)
p_lect.write_bytes(lect.encode("utf-8"))
scellement.sceller(p_lect)
sha_mand_lect = scellement.verifier(p_lect)
print("MANDAT_LECTEUR_SCELLE:", sha_mand_lect)

# Judge mandate (with R-5344 head reserve per R-5345!)
juge_raw = (COND / "projet-mandat-juge-lecture-sondes-v3-brouillon3.md").read_text(encoding="utf-8")
juge = strip_work_header(juge_raw)
reserve_r5344 = (
    "\n> **Réserve de tête sur le registre propre (`R-5344` et `R-5345`, `registres/decisions.md`)** : "
    "une ligne `SPEC-LECTURES-DOMMAGE-DIFFUSION-V5-IIB` ajoutée par erreur à `registres/sondes-iib-v1.md` "
    "au commit `2c4bafafd` (2026-11-24T17:19Z) a été retirée à `17:20Z` (commit `cf216e05d`), écart déclaré à la règle "
    "des lignes ajoutées seulement ; aucune pièce ni aucun arbre n'avait lu le registre entre l'ajout et le retrait.\n"
)
first_nl = juge.index("\n")
juge = juge[:first_nl + 1] + reserve_r5344 + juge[first_nl + 1:]
juge_reps = {
    "<DESIGNATION_JUGE>": "agent neuf, modèle Gemini 4 Neon (autorisé sur le chemin critique de l'entretien du 1er décembre par GO-2026-11-24-49), lancé par la session mère après la lecture et, s'il y en a un, après le scellement du rapport de l'audit, avec ce seul mandat pour consigne",
    "<CHEMIN_LISTE_EXCLUS>": EXCLUS_PATH,
    "<EMPREINTE_LISTE_EXCLUS>": EXCLUS_SHA,
    "<CHEMIN_QUI_A_LU_QUOI>": QLQ_PATH,
    "<EMPREINTE_QUI_A_LU_QUOI>": QLQ_SHA,
    "<ATTESTATION_HORS_EXCLUS>": ATTEST_HORS,
    "<CHEMIN_MANDAT_LECTEUR>": REL_MAND_LECTEUR,
    "<EMPREINTE_MANDAT_LECTEUR>": sha_mand_lect,
    "<EMPREINTE_ETATS>": ETATS_SHA,
    "<EMPREINTE_ATTESTATION_COURSE>": D15_SHA,
    "<REFERENCE_BOITE_NOIRE ou « absente »>": "absente",
    "<HEURE_SCELLEMENT_ADDITIF_2>": "2026-11-24T10:34:26Z",
    "<HEURE_PREMIERE_SORTIE_ETALONNAGE>": "2026-11-22T20:29:04Z",
    "<HEURE_PREMIERE_SORTIE_COURSE_LUE>": "2026-11-23T04:41:59Z",
    "<SOURCE_HEURES>": f"registre des décisions R-5173, R-5223, R-5408, champ AD-3 de l'additif 1 et pièce D-15 ({D15_SHA})",
    "<CHEMIN_VERDICT>": "docs/verdicts/verdict-lecture-sondes-barreau8-v1.md",
}
for k, v in juge_reps.items():
    juge = juge.replace(k, v)
juge = adapt_env(juge).replace("\r\n", "\n")
leftover_j = re.findall(r"<[A-Z][A-Z0-9_]*", juge)
assert not leftover_j, f"Leftover placeholders in judge mandate: {leftover_j}"
p_juge = WT_PUSH / REL_MAND_JUGE
p_juge.write_bytes(juge.encode("utf-8"))
scellement.sceller(p_juge)
sha_mand_juge = scellement.verifier(p_juge)
print("MANDAT_JUGE_SCELLE:", sha_mand_juge)

# 3. Mechanically validate exiger_mandats + exiger_attestation_ordre + exiger_attestation_course + exiger_accord
res_m = ls.exiger_mandats(p_lect, p_juge, EXCLUS_SHA, QLQ_SHA)
ls.exiger_attestation_ordre(WT_PUSH, ls.Pieces(), res_m["texte_du_mandat_du_lecteur"])
ls.exiger_attestation_course(WT_PUSH, ls.Pieces(), res_m["texte_du_mandat_du_lecteur"], "20261123-043944-iib-course-reel", "20261123-043944-iib-course-reel")
ls.exiger_accord(WT_PUSH / "registres/go.md", "GO-2026-11-24-28")
print("ALL_MANDATE_GUARDS_PASSED_100_PERCENT!")

# 4. Append next R-NNNN in decisions.md, commit & push to origin/main
dec_path = WT_PUSH / "registres/decisions.md"
dec_txt = dec_path.read_text(encoding="utf-8")
nums = [int(m.group(1)) for m in re.finditer(r"^- R-(\d+) ", dec_txt, re.M) if int(m.group(1)) < 9000]
next_r = max(nums) + 1
now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
r_line = (
    f"- R-{next_r} ({now_utc}) — Barreau 8, ouverture de la lecture décisive des sondes (GO-2026-11-24-28) : "
    f"recette de puissance `D-10` achevée (`{REL_AIRES}`, SHA-256 `{sha_aires}` ; manifeste `{sha_manif}`), "
    f"mandat du lecteur scellé (`{REL_MAND_LECTEUR}`, `{sha_mand_lect}`) puis mandat du juge scellé avec réserve de tête `R-5344`/`R-5345` "
    f"(`{REL_MAND_JUGE}`, `{sha_mand_juge}`). Toutes les gardes mécaniques (`exiger_mandats`, `exiger_attestation_ordre`, "
    f"`exiger_attestation_course`, `exiger_accord`) conformes. Arbre de lecture propre préparé ; lancement du lecteur neuf."
)
dec_txt = dec_txt.rstrip("\n") + "\n" + r_line + "\n"
dec_path.write_bytes(dec_txt.replace("\r\n", "\n").encode("utf-8"))

git_run(WT_PUSH, "add", "registres/decisions.md",
        REL_AIRES, REL_AIRES + ".sha256",
        REL_MANIF, REL_MANIF + ".sha256",
        REL_MAND_LECTEUR, REL_MAND_LECTEUR + ".sha256",
        REL_MAND_JUGE, REL_MAND_JUGE + ".sha256")
git_run(WT_PUSH, "commit", "-m", f"R-{next_r} : D-10 puissance et mandats v3 lecteur/juge scelles pour lecture barreau 8")
git_run(WT_PUSH, "push", "origin", "HEAD:refs/heads/main")
new_head = git_run(WT_PUSH, "rev-parse", "HEAD").stdout.strip()
print(f"PUSHED_MAIN_OK: R-{next_r} head={new_head}")

# 5. Prepare clean detached reading tree ARBRE (scratch/b8-lecture-arbre)
if ARBRE.exists():
    raise RuntimeError(f"ARBRE already exists: {ARBRE}")
git_run(REPO, "fetch", "origin", "main")
git_run(REPO, "worktree", "add", "--no-checkout", "--detach", str(ARBRE), new_head)
git_run(ARBRE, "sparse-checkout", "init", "--no-cone")
git_run(ARBRE, "sparse-checkout", "set",
        "/*",
        "!/docs/notes/organisme-boucle-reelle-v1/essai-a-blanc-v1/sorties-completes/v64-factice-g2/")
git_run(ARBRE, "checkout")

# Add LIVRAISON-PASSE-IIB to git info/exclude so worktree stays 100% clean
LIV = "versement/20261124-122719-rejeu-activations-voie-a/sortie-passe/livraison"
common_dir = Path(git_run(ARBRE, "rev-parse", "--git-common-dir").stdout.strip())
if not common_dir.is_absolute():
    common_dir = (ARBRE / common_dir).resolve()
excl = common_dir / "info" / "exclude"
excl.parent.mkdir(parents=True, exist_ok=True)
excl_txt = excl.read_text(encoding="utf-8") if excl.exists() else ""
if f"/{LIV}/" not in excl_txt.splitlines():
    excl.write_text(excl_txt.rstrip("\n") + f"\n/{LIV}/\n", encoding="utf-8", newline="\n")

# Extract LIVRAISON-PASSE-IIB via git archive + tarfile (NEVER opening any score file!)
tar_bytes = git_run(REPO, "archive", "--format=tar", "origin/donnees/passe-activations-voie-a-v1", LIV, binary=True).stdout
with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:") as tf:
    tf.extractall(path=ARBRE, filter="data")

# Copy D-8 probe files & verify all 3 hashes
d8_target = ARBRE / "donnees" / "20261114-001352-t07-lecture-reel"
d8_target.mkdir(parents=True, exist_ok=True)
for fname in ("planchers-figees-t07.npz", "planchers-figees-t07.npz.sha256",
              "sondes-neuves-t07.npz", "sondes-neuves-t07.npz.sha256"):
    shutil.copy2(D8_SRC / fname, d8_target / fname)

assert scellement.verifier(d8_target / "planchers-figees-t07.npz") == "94ca013c66e5dbd35b3ea55ec8aa4eb7b299e5dd63a95f7ccea7ced8d120f224"
assert scellement.verifier(d8_target / "sondes-neuves-t07.npz") == "374ad47346ae40d5a4d350724d0d19b5961724066dd7fdfaaf0adf1c3a4cbb79"
assert scellement.verifier(ARBRE / "donnees/20261019-230011-p3-reel/sondes-figees-legeres.npz") == "701f73bd3a8ef30f46b304a6d5caa21444f0e1daf0829d04046e4024aa4e6e60"

st = git_run(ARBRE, "status", "--porcelain", "--untracked-files=all").stdout.strip()
assert not st, f"ARBRE NOT CLEAN: {st[:200]}"
print(f"ARBRE_DE_LECTURE_PRET_ET_PROPRE: {ARBRE} commit={new_head}")
