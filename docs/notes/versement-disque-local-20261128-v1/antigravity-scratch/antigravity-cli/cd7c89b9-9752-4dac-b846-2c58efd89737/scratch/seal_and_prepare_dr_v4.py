import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
SCRATCH = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch")
WT_CODE = SCRATCH / "wt-dr-v3"
WT_LANC = SCRATCH / "wt-lancement-dr-v2"
PY = SCRATCH / "venv-py314" / "Scripts" / "python.exe"


def run(cmd, cwd=None, check=True, env_extra=None):
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONUTF8"] = "1"
    if env_extra:
        env.update(env_extra)
    print("RUN:", cmd)
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    if r.stdout.strip():
        print(r.stdout.strip())
    if r.returncode != 0:
        print("STDERR:", r.stderr.strip(), file=sys.stderr)
        if check:
            sys.exit(r.returncode)
    return r


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_lf_sealed(path: Path, text: str) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = text.replace("\r\n", "\n").encode("utf-8")
    path.write_bytes(data)
    h = sha256_bytes(data)
    comp = Path(str(path) + ".sha256")
    comp.write_bytes(f"{h}  {path.name}\n".encode("utf-8"))
    return h


def main():
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    c_new = run(["git", "-C", str(WT_CODE), "rev-parse", "HEAD"]).stdout.strip()
    assert len(c_new) == 40, f"Bad commit {c_new}"
    print("C_NEW =", c_new)

    # Verify C_NEW is descendant of 6b2b821a
    run(["git", "-C", str(WT_CODE), "merge-base", "--is-ancestor", "6b2b821a28f8bebebae2188d9f020ce731464306", c_new])

    # Verify hashes of code and tests at C_NEW
    code_paths = [
        "scripts/amorce_instance_dose_reponse_v4.sh",
        "scripts/ecrire_configuration_dose_reponse_v3.py",
        "scripts/lancer_dose_reponse_v4.sh",
        "src/controle_ia/dose_reponse/__init__.py",
        "src/controle_ia/dose_reponse/conditions_v1.py",
        "src/controle_ia/dose_reponse/controles_v3.py",
        "src/controle_ia/dose_reponse/course_v3.py",
        "src/controle_ia/dose_reponse/extraction_v1.py",
        "src/controle_ia/dose_reponse/lecture_v2.py",
    ]
    test_paths = [
        "scripts/tests-cibles-dose-reponse-v4.txt",
        "tests/factice_dose_reponse_v1.py",
        "tests/test_dose_reponse_amorce_v4.py",
        "tests/test_dose_reponse_v3.py",
    ]

    def git_blob_sha(rel: str) -> str:
        b = subprocess.check_output(["git", "-C", str(WT_CODE), "show", f"{c_new}:{rel}"])
        return sha256_bytes(b)

    code_map = {p: git_blob_sha(p) for p in code_paths}
    test_map = {p: git_blob_sha(p) for p in test_paths}
    sha_dev = git_blob_sha("docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md")
    sha_cl = git_blob_sha("docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md")
    print("AMORCE_V4_SHA256 =", code_map["scripts/amorce_instance_dose_reponse_v4.sh"])
    print("DEV_REPORT_SHA =", sha_dev)
    print("CL_REPORT_SHA =", sha_cl)

    # Copy dev & review reports to main
    for rel in (
        "docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md",
        "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md",
    ):
        for suffix in ("", ".sha256"):
            src = WT_CODE / (rel + suffix)
            dst = REPO / (rel + suffix)
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())

    # 1. Write & seal CODE-DOSE-REPONSE-CONSIGNE-CACHEE-<C_NEW>-v3.json
    code_json_rel = f"registres/code-dose-reponse-consigne-cachee/CODE-DOSE-REPONSE-CONSIGNE-CACHEE-{c_new}-v3.json"
    code_doc = {
        "branche": "code/dose-reponse-consigne-cachee-v1",
        "changement_depuis_v2": (
            "Écart matériel minimal autorisé par Lazar (GO-2026-11-25-01, R-5397) : relèvement de "
            "`stockage_max_usd_h` de 0,08 à 0,10 USD/h (fichiers neufs R12 : `controles_v3.py`, "
            "`course_v3.py`, `ecrire_configuration_dose_reponse_v3.py`, `amorce_instance_dose_reponse_v4.sh`, "
            "`lancer_dose_reponse_v4.sh`, `tests-cibles-dose-reponse-v4.txt` à 60 essais attendus). "
            "Tous les fichiers antérieurs, `lecture_v2.py` et `lecteur_texte_dose_reponse_v2.py` restent intacts."
        ),
        "chemin_propose": code_json_rel,
        "code": code_map,
        "commandes": {
            "amorce": "scripts/amorce_instance_dose_reponse_v4.sh",
            "configuration": "scripts/ecrire_configuration_dose_reponse_v3.py",
            "course": "python -m controle_ia.dose_reponse.course_v3",
            "lanceur": "scripts/lancer_dose_reponse_v4.sh",
            "lecture": "python -m controle_ia.dose_reponse.lecture_v2",
        },
        "commit": c_new,
        "contre_lectures": [
            {
                "chemin": "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-1-code-dose-reponse-v1.md",
                "objet": "code v1 → v2",
                "sha256": "ad2dac0ac17d710530b425148d08952f15571750c14ec79ff4d7cb621f8cea5f",
            },
            {
                "chemin": "docs/notes/code-dose-reponse-consigne-cachee-v1/verification-1-code-dose-reponse-v1.md",
                "objet": "vérification v2",
                "sha256": "b56249e9f0248a14d62449fede7be44000ec0800f340b6b248424fcfc1ad6b3a",
                "verdict": "prêt",
            },
            {
                "chemin": "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-1-lecteur-texte-et-amorce-v3-v1.md",
                "objet": "amorce v3 (et lecteur du texte)",
                "sha256": "cabdf1356330a29a4447cae780e809a14dac45e955d21bf0a3ab2b916c288f0a",
                "verdict": "amorce v3 prête, aucun défaut",
            },
            {
                "chemin": "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md",
                "objet": "écart matériel minimal stockage 0,08 → 0,10 (GO-2026-11-25-01, amorce v4, controles_v3, course_v3, lanceur v4)",
                "sha256": sha_cl,
                "verdict": "prêt",
            },
        ],
        "declaration": (
            "Aucune action n'a été générée sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test "
            "(a68468fe…) par le développeur (93b2a51f), le contre-lecteur neuf (a7746c4f) ni la session mère de lancement "
            "(Antigravity Gemini 4 Neon cd7c89b9) ; modèle jouet et textes factices seulement."
        ),
        "essais": test_map,
        "essais_resultat": "60 essais collectés (47 + 13) ; 59/60 verts sous Windows (1 particularité MSYS/cp1252 sur code inchangé), 60 attendus sous Linux",
        "ligne": "CODE-DOSE-REPONSE-CONSIGNE-CACHEE",
        "note_chemin": "le chemin porte le commit complet du code : `controles_v3.controler_registre` exige qu'une ligne CODE-DOSE-REPONSE-CONSIGNE-CACHEE cite `commit_code`",
        "reserves": [
            "V2-01 à V2-04 de la pièce v1, inchangées",
            "la création exige les quatre lignes nommées par `designation_critere_3.lignes_registre` (CL-06 de la contre-lecture du lecteur)",
            "écart matériel minimal stockage_max_usd_h = 0,10 USD/h autorisé par GO-2026-11-25-01 (R-5397) ; jeton gh autorisé avec révocation post-course par GO-2026-11-25-02 (R-5399)",
        ],
        "texte_de_designation": {
            "chemin": "prereg/G0-critere-3-designation-course-v1.md",
            "sha256": "19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31",
        },
        "texte_scelle": {
            "chemin": "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
            "sha256": "2263c5c447d17e0d2b045ba1a6421c681809df2ec8bafbcc3226aa6dd3f31c41",
        },
        "version": (
            "v3 (course désignée pour le critère 3, option A, GO-2026-11-24-31 ; stockage 0,10 USD/h GO-2026-11-25-01) ; "
            "remplace pour le lancement les pièces v1 et v2, qui restent inscrites"
        ),
    }
    sha_code_json = write_lf_sealed(
        REPO / code_json_rel,
        json.dumps(code_doc, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
    )

    # 2. Write & seal ordre-de-lancement-dose-reponse-v6-erratum-1.md
    erratum_rel = "docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-dose-reponse-v6-erratum-1.md"
    erratum_txt = f"""# Erratum 1 à l'ordre de lancement v6 — course de dose–réponse de l'organisme à consigne cachée

> Pièce de classe A (erratum matériel minimal à `docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-dose-reponse-v6-scelle.md`, empreinte `08cb2b355c595254750819db4d7fdf0bf9b46593abf2f77ed5fd1e62bfaf68cc`, qui reste intacte sous R12). Scellée par la session mère Antigravity (`cd7c89b9-9752-4dac-b846-2c58efd89737`, Gemini 4 Neon) le `{now_utc}`.

## Objet (seuls changements autorisés par Lazar)

1. **Borne de stockage (`GO-2026-11-25-01`, `R-5397`)** : `offre.stockage_max_usd_h` passe de `0,08` à **`0,10` USD de l'heure** (tarif standard Vast.ai `0,20 USD/Go/mois = 0,0822 USD/h` sur 300 Go). Toutes les autres bornes restent strictement inchangées : une `A100 SXM4 80 Go`, carte ≤ `1,30 USD/h`, 16 cœurs, 128 000 Mo de mémoire vive, disque ≥ `300 Go`, téléchargement ≤ `0,05 USD/Go`, plafond cumulé **`90 USD`** (`GO-2026-11-24-25`), alerte unique à `72 USD`, dernier jour de création `2026-12-12`.
2. **Code versionné R12 (`CODE-DOSE-REPONSE-CONSIGNE-CACHEE` v3)** : commit `{c_new}` (descendant direct de `6b2b821a28f8bebebae2188d9f020ce731464306` ; les quatre lignes de `DESIGNATION-CRITERE-3`, `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE`, `SONDES-LUES-CRITERE-3` et `CODE-MOTS-ET-COUT-T06` restent 100 % intactes) :
   - pièce de registre : `{code_json_rel}` (`{sha_code_json}`) ;
   - contre-lecture classe B (Gemini 4 Neon neuf, verdict **`prêt`**, 0 bloquant, 0 majeur) : `docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md` (`{sha_cl}`) ;
   - amorce v4 : `scripts/amorce_instance_dose_reponse_v4.sh` (`{code_map['scripts/amorce_instance_dose_reponse_v4.sh']}`) ;
   - lanceur v4 : `scripts/lancer_dose_reponse_v4.sh` (`{code_map['scripts/lancer_dose_reponse_v4.sh']}`) ;
   - configuration v2 : `prereg/T0.6-dose-reponse-configuration-course-v2.json`, écrite par `scripts/ecrire_configuration_dose_reponse_v3.py` (`{code_map['scripts/ecrire_configuration_dose_reponse_v3.py']}`) ;
   - branche de lancement neuve (R12) : `lancement/dose-reponse-v2`, tirée du commit `{c_new}` ;
   - lecture hors ligne inchangée (`controle_ia.dose_reponse.lecture_v2`) ; lecteur du texte inchangé (`scripts/lancer_lecteur_texte_dose_reponse_v2.sh`).
3. **Session de lancement et jeton GitHub (`GO-2026-11-25-02`, `R-5399`)** :
   - déclaration de session de lancement v2 : `registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v2.json` (session mère Antigravity `cd7c89b9-9752-4dac-b846-2c58efd89737`) ;
   - jeton GitHub transmis à l'instance Vast.ai (masqué, jamais affiché) : jeton `gh` du trousseau local autorisé par `GO-2026-11-25-02`, avec obligation de révocation immédiate après versement prouvé de la course (rappel inscrit dans `registres/rappels.md`).
4. **Rien d'autre ne change** par rapport à `ordre-de-lancement-dose-reponse-v6-scelle.md` (`08cb2b35…`).
"""
    sha_erratum = write_lf_sealed(REPO / erratum_rel, erratum_txt)

    # 3. Write & seal DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v2.json
    decl_rel = "registres/code-dose-reponse-consigne-cachee/DECLARATION-SESSION-LANCEMENT-DOSE-REPONSE-v2.json"
    decl_doc = {
        "cle": "DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE",
        "session_de_lancement": "session mère Antigravity cd7c89b9-9752-4dac-b846-2c58efd89737",
        "modele": "Gemini 4 Neon (Antigravity)",
        "phrase": "aucune action générée sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test (a68468fe…)",
        "declaration_mot_pour_mot": "Je déclare n'avoir généré aucune action sous un texte de la pièce jointe (7a5f633c…) ni du fichier du premier test (a68468fe…)",
        "recue_le": f"{now_utc} (déclaration directe de la session mère de lancement)",
        "renvoi_ligne_code": {
            "cle": "CODE-DOSE-REPONSE-CONSIGNE-CACHEE",
            "chemin": code_json_rel,
            "sha256": sha_code_json,
            "commit_code": c_new,
        },
        "ordre": {
            "chemin": "docs/notes/code-dose-reponse-consigne-cachee-v1/ordre-de-lancement-dose-reponse-v6-scelle.md",
            "sha256": "08cb2b355c595254750819db4d7fdf0bf9b46593abf2f77ed5fd1e62bfaf68cc",
            "erratum_1": {
                "chemin": erratum_rel,
                "sha256": sha_erratum,
            },
        },
        "inscrite_par": "session mère Antigravity cd7c89b9-9752-4dac-b846-2c58efd89737",
        "inscrite_le": now_utc,
    }
    sha_decl = write_lf_sealed(
        REPO / decl_rel,
        json.dumps(decl_doc, ensure_ascii=False, indent=1) + "\n",
    )

    # 4. Append 3 lines to registres/scellements-v1.md and R-5402 to registres/decisions.md
    scel_path = REPO / "registres/scellements-v1.md"
    scel_txt = scel_path.read_text(encoding="utf-8")
    if not scel_txt.endswith("\n"):
        scel_txt += "\n"
    scel_lines = (
        f"| CODE-DOSE-REPONSE-CONSIGNE-CACHEE | {now_utc} | {code_json_rel} | {sha_code_json} |\n"
        f"| ORDRE-LANCEMENT-DOSE-REPONSE-ERRATUM-1 | {now_utc} | {erratum_rel} | {sha_erratum} |\n"
        f"| DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE | {now_utc} | {decl_rel} | {sha_decl} |\n"
    )
    scel_path.write_bytes((scel_txt + scel_lines).replace("\r\n", "\n").encode("utf-8"))

    dec_path = REPO / "registres/decisions.md"
    dec_txt = dec_path.read_text(encoding="utf-8")
    if not dec_txt.endswith("\n"):
        dec_txt += "\n"
    r5402 = (
        f"- R-5402 ({now_utc}) — Dose-réponse de l'organisme à consigne cachée (GO-2026-11-24-25, GO-2026-11-25-01, GO-2026-11-25-02) : "
        f"écart matériel minimal `stockage_max_usd_h` 0,08 → 0,10 USD/h en fichiers neufs R12 committé et poussé sur "
        f"`code/dose-reponse-consigne-cachee-v1` (commit `{c_new}`, descendant de `6b2b821a` ; `CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE` et les "
        f"quatre lignes de `DESIGNATION-CRITERE-3` 100 % intacts) après contre-lecture classe B par un agent neuf (Gemini 4 Neon `a7746c4f`, "
        f"verdict **`prêt`**, 0 bloquant, 0 majeur, rapport `{sha_cl[:8]}…`). Pièces scellées et inscrites au registre des scellements : "
        f"`CODE-DOSE-REPONSE-CONSIGNE-CACHEE` v3 (`{sha_code_json[:8]}…`), `ORDRE-LANCEMENT-DOSE-REPONSE-ERRATUM-1` (`{sha_erratum[:8]}…`), "
        f"`DECLARATION-LANCEMENT-DOSE-REPONSE-CONSIGNE-CACHEE` v2 (`{sha_decl[:8]}…`, mère Antigravity `cd7c89b9`). Branche de lancement "
        f"`lancement/dose-reponse-v2` préparée pour création Vast.ai.\n"
    )
    dec_path.write_bytes((dec_txt + r5402).replace("\r\n", "\n").encode("utf-8"))

    # Commit & push main
    run([
        "git", "-C", str(REPO), "add", "--",
        code_json_rel, code_json_rel + ".sha256",
        erratum_rel, erratum_rel + ".sha256",
        decl_rel, decl_rel + ".sha256",
        "docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md",
        "docs/notes/code-dose-reponse-consigne-cachee-v1/rapport-developpeur-stockage-010-v1.md.sha256",
        "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md",
        "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md.sha256",
        "registres/scellements-v1.md",
        "registres/decisions.md",
    ])
    run([
        "git", "-C", str(REPO), "commit", "-m",
        f"Scellement CODE dose-réponse v3 ({c_new[:8]}), erratum 1 ordre v6 et déclaration v2 (GO-2026-11-25-01, R-5402)",
    ])
    run([
        "git", "-C", str(REPO), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
        "push", "origin", "main",
    ])

    # 5. Create launch branch lancement/dose-reponse-v2 from C_NEW in WT_LANC
    if WT_LANC.exists():
        run(["git", "-C", str(REPO), "worktree", "remove", "--force", str(WT_LANC)])
    run([
        "git", "-C", str(REPO), "-c", "core.protectNTFS=false", "worktree", "add",
        "--no-checkout", "-B", "lancement/dose-reponse-v2", str(WT_LANC), c_new,
    ])
    run(["git", "-C", str(WT_LANC), "config", "core.longpaths", "true"])
    run(["git", "-C", str(WT_LANC), "sparse-checkout", "init", "--no-cone"])
    p_sc = subprocess.run(
        ["git", "-C", str(WT_LANC), "sparse-checkout", "set", "--no-cone", "--stdin"],
        input="/*\n!/docs/notes/organisme-boucle-reelle-v1/essai-a-blanc-v1/sorties-completes/v64-factice-g2/\n",
        text=True, capture_output=True,
    )
    assert p_sc.returncode == 0, p_sc.stderr
    run(["git", "-C", str(WT_LANC), "-c", "core.protectNTFS=false", "checkout"])

    # Checkout ONLY data & register files from origin/main and origin/banque/dose-reponse-consigne-cachee-v1
    run(["git", "-C", str(WT_LANC), "checkout", "origin/main", "--",
         "registres/go.md", "registres/scellements-v1.md",
         "prereg/G0-critere-3-designation-course-v1.md", "prereg/G0-critere-3-designation-course-v1.md.sha256",
         "registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json",
         "registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json.sha256",
         "registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md",
         "registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md.sha256",
         code_json_rel, code_json_rel + ".sha256",
         decl_rel, decl_rel + ".sha256",
         erratum_rel, erratum_rel + ".sha256",
         "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md",
         "docs/notes/code-dose-reponse-consigne-cachee-v1/contre-lecture-stockage-010-neon-v1.md.sha256"])
    run(["git", "-C", str(WT_LANC), "checkout", "origin/banque/dose-reponse-consigne-cachee-v1", "--",
         "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json",
         "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256"])

    # Write designation JSON to scratch and run ecrire_configuration_dose_reponse_v3.py
    des_path = SCRATCH / "designation-critere-3.json"
    des_path.write_bytes(
        (json.dumps({
            "chemin": "prereg/G0-critere-3-designation-course-v1.md",
            "sha256": "19dbc99edb551a4e1bbbef0ea28a5a860bd739b69d84d60ccf43c2de03125c31",
            "lignes_registre": [
                "DESIGNATION-CRITERE-3",
                "CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE",
                "SONDES-LUES-CRITERE-3",
                "CODE-MOTS-ET-COUT-T06",
            ],
        }) + "\n").encode("utf-8")
    )
    run([
        str(PY), "scripts/ecrire_configuration_dose_reponse_v3.py",
        "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json",
        c_new, "--designation", str(des_path),
    ], cwd=str(WT_LANC), env_extra={"PYTHONPATH": "src"})

    # Verify zero code diff vs C_NEW
    run(["git", "-C", str(WT_LANC), "diff", "--quiet", c_new, "--",
         "src", "scripts", "tests", ".claude", "pyproject.toml", "requirements-*.txt"])

    # Add & commit & push lancement/dose-reponse-v2
    run(["git", "-C", str(WT_LANC), "add", "-f", "--",
         "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json",
         "donnees/20261124-144844-banque-dose-reponse-extraction-v2/taches-banque.json.sha256",
         "prereg/T0.6-dose-reponse-configuration-course-v2.json",
         "prereg/T0.6-dose-reponse-configuration-course-v2.json.sha256",
         "prereg/G0-critere-3-designation-course-v1.md", "prereg/G0-critere-3-designation-course-v1.md.sha256",
         "registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json",
         "registres/code-lecteur-du-texte-dose-reponse/CODE-LECTEUR-DU-TEXTE-DOSE-REPONSE-6b2b821a28f8bebebae2188d9f020ce731464306-v1.json.sha256",
         "registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md",
         "registres/sondes-lues-critere-3/SONDES-LUES-CRITERE-3-v1.md.sha256",
         code_json_rel, code_json_rel + ".sha256",
         decl_rel, decl_rel + ".sha256",
         erratum_rel, erratum_rel + ".sha256",
         "registres/go.md", "registres/scellements-v1.md"])
    run(["git", "-C", str(WT_LANC), "commit", "-m",
         "Lancement v2 course dose-réponse désignée (stockage 0,10, GO-2026-11-25-01) : config v2, banque, désignation, registres"])
    l_new = run(["git", "-C", str(WT_LANC), "rev-parse", "HEAD"]).stdout.strip()
    run([
        "git", "-C", str(WT_LANC), "-c", "credential.helper=", "-c", "credential.helper=!gh auth git-credential",
        "push", "-u", "origin", "lancement/dose-reponse-v2",
    ])
    print("L_NEW =", l_new)

    # 6. Run verifier-code + full controles_v3 pre-creation checks in WT_LANC!
    run([str(PY), "-P", "-B", "scripts/lecteur_texte_dose_reponse_v2.py", "verifier-code"],
        cwd=str(WT_LANC), env_extra={"PYTHONPATH": "src"})

    check_code = """
import json, sys
from pathlib import Path
from controle_ia.scellement import verifier
from controle_ia.dose_reponse import controles_v3 as ct
from controle_ia.lancement_t08 import session_v1 as s8
cfg = "prereg/T0.6-dose-reponse-configuration-course-v2.json"
verifier(cfg)
c = json.load(open(cfg, encoding="utf-8"))
assert c["mode"] == "reel"
ct.exiger_calendrier("2026-11-25")
r = ct.controles_avant_depense(Path("."), c)
print("CONTROLES_V3_OK:", r["banque"], r["registre"])
t = ct.controler_textes_avant_creation(Path("."), c, ct.charger_tokeniseur_agent(c))
print("TEXTES_OK:", t)
g = s8.go_t08("registres/go.md", cfg, "GO-2026-11-24-25", "2026-11-25")
cal = s8.calendrier("registres/go.md", cfg, "GO-2026-11-24-25", "2026-11-25")
print("GO_OK:", g)
print("CAL_OK:", cal)
"""
    run([str(PY), "-B", "-c", check_code], cwd=str(WT_LANC), env_extra={"PYTHONPATH": "src"})

    # Save launch metadata JSON for creation script
    meta = {
        "C_NEW": c_new,
        "L_NEW": l_new,
        "BRANCHE_LANCEMENT": "lancement/dose-reponse-v2",
        "AMORCE_V4_SHA256": code_map["scripts/amorce_instance_dose_reponse_v4.sh"],
        "CONFIG": "prereg/T0.6-dose-reponse-configuration-course-v2.json",
        "PREREG": "prereg/T0.6-organisme-consigne-cachee-dose-reponse-v1.md",
        "BRANCHE_SORTIE": "calcul/dose-reponse-v1",
        "GO_ID": "GO-2026-11-24-25",
    }
    (SCRATCH / "dr-launch-meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print("SEAL_AND_PREPARE_ALL_OK")


if __name__ == "__main__":
    main()
