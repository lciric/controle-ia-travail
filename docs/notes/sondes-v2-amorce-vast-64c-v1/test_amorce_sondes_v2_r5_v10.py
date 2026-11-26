"""Essais R5 unitaires et d'intégration de `amorce-sondes-v2-v3.sh` (GO-2026-11-24-02 / GO-2026-11-24-15).

Exécutable aussi bien avec `pytest` qu'en script autonome (`python test_amorce_sondes_v2_r5_v3.py`).

Couvre :
  1. Contrôles statiques et structurels stricts de `amorce-sondes-v2-v3.sh` :
     - fins de ligne LF strictes (aucun `\\r`) ;
     - résolution de `CPU_DISPO` (`nproc --all`) et `N_WORKERS` strictement AVANT `export OMP_NUM_THREADS=1`
       (`OPENBLAS_NUM_THREADS=1`, `MKL_NUM_THREADS=1`, `NUMEXPR_NUM_THREADS=1`) + garde `EXIGER_MULTICOEUR` ;
     - absence de `xargs ... -n 1 ... -I {}` (correction de l'avertissement GNU xargs) ;
     - `PAS_ETALON=6` par défaut avec dernière tranche bornée à `500` (`[496, 500)`, 62 tranches sur `[130, 500)`) ;
     - exécution en tâche de fond parallèle de `sonde_complet_1rep` sur le 63e cœur lorsque `N_WORKERS >= 63` ;
     - garde `BRANCHE_SORTIE` (défaut `calcul/sondes-v2-epreuve-plantee-v4-suite`, refus de `main` et de
       `calcul/sondes-v2-epreuve-plantee-v4`) ;
     - compatibilité conteneur Vast.ai (`GH_TOKEN_ENV` / `VAST_API_KEY_ENV` -> fichiers `0600` puis `unset`
       complet des variables secrètes exportées ; `apt-get` auto pour `git`, `curl`, `ca-certificates`, `procps`,
       `time` ; fallback `CONTAINER_ID` strictement numérique ; liste noire des 5 instances Vast.ai intouchables
       `58936096`, `58936099`, `58936100`, `60988826`, `62498862`) ;
     - masquage et contrôle anti-fuite de `GH_TOK`, `HCLOUD_TOKEN` et `VAST_API_KEY`.
  2. Vérification mathématique et en Python pur de `programme_monde_plante_v4.fusionner()` et
     `ecrire_synthese_fusionnee()` (depuis un clone temporaire détaché au commit figé `0ce9e35110d9…`, sans
     toucher au dépôt principal R12) :
     - mini-cas `repliques=25` découpé en largeurs mixtes `[0, 10)`, `[10, 20)`, `[20, 25)` : synthèse identique
       à l'octet à un processus unique `[0, 25)` ;
     - mini-cas `repliques=26` reproduisant le découpage `PAS_ETALON=6` avec dernière tranche de largeur 4
       (`[0, 10)` largeur 10 + `[10, 16)` largeur 6 + `[16, 22)` largeur 6 + `[22, 26)` largeur 4) : synthèse
       identique à l'octet à un processus unique `[0, 26)` ;
     - gardes négatives de `fusionner()` (trou dans les plages, couverture incomplète, discordance du chemin de
       `note_effectifs`) ;
     - vérification des 13 rapports étalon amont réels (`[0, 130)`) si accessibles localement et preuve que
       l'union des 13 tranches `[0, 130)` (pas 10) et des 62 tranches `[130, 500)` (`PAS_ETALON=6`, dernière
       tranche `[496, 500)` de 4 répliques) forme 75 tranches disjointes couvrant exactement `[0, 500)`.
  3. Essais dynamiques bout-en-bout sous `bash` (si un environnement `bash` + `git` + `curl` + `sha256sum` + `tar`
     est disponible) :
     - `bash -n amorce-sondes-v2-v3.sh` ;
     - rejets immédiats des gardes (`EXIGER_MULTICOEUR=1` avec `N_WORKERS=1`, `REPO_URL` avec jeton,
       `BRANCHE_SORTIE=main`, `BRANCHE_SORTIE=calcul/sondes-v2-epreuve-plantee-v4`, chacune des 5 instances Vast.ai
       intouchables via `VAST_INSTANCE_ID` et via `CONTAINER_ID`, identifiant Vast non numérique ou préfixé de `0`) ;
     - scénario Vast.ai 64 cœurs (`MODE_RUN=etalon_suite_et_sonde_complet_1rep`, `N_WORKERS=64`, `PAS_ETALON=6`,
       `GH_TOKEN_ENV`, `VAST_API_KEY_ENV`, `CONTAINER_ID` numérique) : reprise `[0, 130)` sans recalcul, parallélisme
       effectif sonde + étalon, absence totale des secrets dans `os.environ` des fils Python, masquage anti-fuite,
       `100 %` `.sha256` valides, préservation intacte de `calcul/sondes-v2-epreuve-plantee-v4` et `DELETE` Vast.ai ;
     - scénario Hetzner (`MODE_RUN=etalon_suite_et_complet` avec minuterie R10 `rc=124` + `DELETE` Hetzner).
"""
from __future__ import annotations

import base64
import hashlib
import http.server
import json
import os
import re
import io
import shutil
import stat
import tarfile
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

DOSSIER_COURANT = Path(__file__).resolve().parent
SCRIPT_AMORCE = DOSSIER_COURANT / "amorce-sondes-v2-v7.sh"

BRAIN_PARENT = DOSSIER_COURANT.parent.parent
SCRATCH_LECTURE_ETALON = BRAIN_PARENT / "scratch" / "lecture-sondes-v2-etalon"
CODE_V2_EXTRAIT = SCRATCH_LECTURE_ETALON / "code-v2"
BRUT_ETALON_AMONT = SCRATCH_LECTURE_ETALON / "brut" / "epreuve-plantee-v4" / "etalon"

REPO_PRINCIPAL = Path(r"C:\Users\lciri\OneDrive\Documents\controle-ia-travail")
if not REPO_PRINCIPAL.exists():
    for p_cand in Path(__file__).resolve().parents:
        if (p_cand / "src" / "controle_ia" / "gardes.py").is_file():
            REPO_PRINCIPAL = p_cand
            break

ENTROPIE_OFFICIELLE = "305159624078239919914131004197200342142"
COMMIT_CODE_OFFICIEL = "0ce9e35110d93dd916e85b1191a2613b101e772d"
SHA_VERITES_OFFICIEL = "b310e1af50459b78833fcc509298bbc1807f1905631e1152b3e28f538f233533"
SHA_NOTE_OFFICIEL = "7338a3dcafb18bfd6fdd43e377bfa0b67f3f6812596749646d6fb0e9c3444db5"
COMMIT_AMONT_ETALON_OFFICIEL = "38c6f4a7054b14b56be7b357c08db8bf11931ca2"
VAST_BLACKLIST = ("58936096", "58936099", "58936100", "60988826", "62498862")

FAKE_GH_TOKEN = "ghp_TESTSECRET_V3_998877"
FAKE_HCLOUD_TOKEN = "hc_TESTHCLOUD_V3_654321"
FAKE_VAST_KEY = "vast_TESTAPIKEY_V3_1122334455"
FAKE_HETZNER_ID = "99887766"
FAKE_VAST_ID = "77889900"



def _rmtree_win(p):
    def _onexc(func, path, exc):
        os.chmod(path, stat.S_IWRITE)
        func(path)
    shutil.rmtree(p, onexc=_onexc)

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def decouper_plages_comme_amorce(de_global: int, a_global: int, pas: int) -> list[tuple[int, int]]:
    """Reproduit exactement `seq de_global pas (a_global - 1)` + `a = min(a_global, de + pas)` de l'amorce v3."""
    assert 0 <= de_global <= a_global <= 500 and pas >= 1
    out: list[tuple[int, int]] = []
    for de in range(de_global, a_global, pas):
        a = min(a_global, de + pas)
        out.append((de, a))
    return out


# ---------------------------------------------------------------------------
# 1. CONTRÔLES STATIQUES ET STRUCTURELS STRICTS DE amorce-sondes-v2-v3.sh
# ---------------------------------------------------------------------------


def test_amorce_v3_lf_strict_et_encodage_utf8() -> None:
    assert SCRIPT_AMORCE.is_file(), f"Script absent : {SCRIPT_AMORCE}"
    raw = SCRIPT_AMORCE.read_bytes()
    assert b"\r" not in raw, "ERREUR : présence de CR (\\r) dans amorce-sondes-v2-v3.sh (LF strict exigé)"
    assert raw.startswith(b"#!/usr/bin/env bash\n"), "Shebang bash LF attendu en ligne 1"
    assert raw.endswith(b"\n"), "Fin de fichier LF attendue"
    texte = raw.decode("utf-8")
    assert len(texte.splitlines()) >= 350


def test_amorce_v3_ordre_nproc_avant_omp_et_garde_multicoeur() -> None:
    texte = SCRIPT_AMORCE.read_text(encoding="utf-8")

    m_cpu = re.search(r'^CPU_DISPO="\$\(nproc --all 2>/dev/null \|\| getconf _NPROCESSORS_ONLN \|\| echo 1\)"$', texte, re.M)
    assert m_cpu is not None, "Expression exacte CPU_DISPO avec `nproc --all` absente"

    m_workers = re.search(r'^N_WORKERS="\$\{N_WORKERS:-\$CPU_DISPO\}"$', texte, re.M)
    assert m_workers is not None, "Affectation N_WORKERS=${N_WORKERS:-$CPU_DISPO} absente"

    m_exiger = re.search(r'^EXIGER_MULTICOEUR="\$\{EXIGER_MULTICOEUR:-1\}"$', texte, re.M)
    assert m_exiger is not None, "Affectation EXIGER_MULTICOEUR=${EXIGER_MULTICOEUR:-1} absente"

    for var_thr in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        m_thr = re.search(rf"^export {var_thr}=1$", texte, re.M)
        assert m_thr is not None, f"export {var_thr}=1 absent"
        assert m_cpu.start() < m_workers.start() < m_thr.start(), (
            f"CPU_DISPO et N_WORKERS doivent être résolus AVANT export {var_thr}=1"
        )

    assert '"$EXIGER_MULTICOEUR" = "1"' in texte and '"$N_WORKERS" -lt 2' in texte


def test_amorce_v3_xargs_sans_n1_avec_replace_et_pas_etalon_6() -> None:
    texte = SCRIPT_AMORCE.read_text(encoding="utf-8")

    # Aucune ligne ne doit combiner xargs avec -n / --max-args ET -I
    for num, ligne in enumerate(texte.splitlines(), 1):
        if "xargs" in ligne and "-I" in ligne:
            assert not re.search(r"(?:^|\s)(?:-n\s*\d+|--max-args)", ligne), (
                f"Ligne {num} combine xargs -n/--max-args et -I : {ligne!r}"
            )
    assert re.search(r'xargs -P "\$workers_locaux" -I \{\}', texte) is not None

    # PAS_ETALON par défaut à 6 (62 tranches sur [130, 500) avec dernière tranche bornée à 500)
    assert 'PAS_ETALON="${PAS_ETALON:-6}"' in texte
    assert 'ETALON_DE="${ETALON_DE:-130}"' in texte
    assert 'ETALON_A="${ETALON_A:-500}"' in texte
    assert "a=$(( de + pas_local > plafond ? plafond : de + pas_local ))" in texte

    # Vérification arithmétique du découpage 64 cœurs : 13 tranches amont + 62 tranches nouvelles = 75 tranches
    amont = decouper_plages_comme_amorce(0, 130, 10)
    suite = decouper_plages_comme_amorce(130, 500, 6)
    assert len(amont) == 13 and amont[0] == (0, 10) and amont[-1] == (120, 130)
    assert len(suite) == 62
    assert suite[0] == (130, 136)
    assert suite[-2] == (490, 496)
    assert suite[-1] == (496, 500), f"Dernière tranche attendue (496, 500) de 4 répliques, obtenu {suite[-1]}"
    toutes = amont + suite
    assert len(toutes) == 75
    bout = 0
    for d, a in toutes:
        assert d == bout
        bout = a
    assert bout == 500

    # Vérification analogue si PAS_ETALON=5 : 13 + 74 = 87 tranches couvrant [0, 500)
    suite_5 = decouper_plages_comme_amorce(130, 500, 5)
    assert len(suite_5) == 74 and suite_5[-1] == (495, 500)

    # Ne jamais supposer len(chemins) == 50 dans le code exécutable
    lignes_hors_commentaires = "\n".join(
        l for l in texte.splitlines() if not l.lstrip().startswith("#")
    )
    assert "len(chemins) == 50" not in lignes_hors_commentaires
    assert "p.ecrire_synthese_fusionnee(" in lignes_hors_commentaires


def test_amorce_v3_gardes_securite_branches_vast_et_63e_coeur() -> None:
    texte = SCRIPT_AMORCE.read_text(encoding="utf-8")

    # Branche amont épinglée et branche de sortie dédiée R12
    assert f'COMMIT_AMONT_ETALON="${{COMMIT_AMONT_ETALON:-{COMMIT_AMONT_ETALON_OFFICIEL}}}"' in texte
    assert 'BRANCHE_AMONT_ETALON="${BRANCHE_AMONT_ETALON:-calcul/sondes-v2-epreuve-plantee-v4}"' in texte
    assert 'BRANCHE_SORTIE="${BRANCHE_SORTIE:-calcul/sondes-v2-epreuve-plantee-v4-suite}"' in texte
    assert "main|master|HEAD|calcul/sondes-v2-epreuve-plantee-v4" in texte

    # Liste noire complète des 5 instances Vast.ai intouchables
    for vid in VAST_BLACKLIST:
        assert vid in texte, f"Instance Vast.ai intouchable {vid} manquante dans amorce-sondes-v2-v3.sh"

    # Gestion conteneur Vast.ai : GH_TOKEN_ENV / VAST_API_KEY_ENV -> 0600 + unset complet + apt-get + CONTAINER_ID
    assert "GH_TOKEN_ENV" in texte and "VAST_API_KEY_ENV" in texte
    assert "chmod 0600" in texte and "chmod 0700" in texte
    assert "unset GH_TOKEN_ENV VAST_API_KEY_ENV HCLOUD_TOKEN_ENV GITHUB_TOKEN GH_TOKEN VAST_API_KEY HCLOUD_TOKEN GH_TOK" in texte
    for pkg in ("git", "curl", "ca-certificates", "procps", "time"):
        assert pkg in texte, f"Paquet système requis {pkg!r} absent de l'installation apt-get"
    assert "CONTAINER_ID" in texte
    assert "https://console.vast.ai/api/v0" in texte
    assert "/instances/${TARGET_VAST_ID}/" in texte
    assert "/servers/${SERVER_ID}" in texte

    # Modes et parallélisme sur le 63e cœur lorsque N_WORKERS >= 63
    for mode in ("etalon_suite_seul", "etalon_suite_et_sonde_complet_1rep", "etalon_suite_et_complet"):
        assert mode in texte
    assert '"$N_WORKERS" -ge 63' in texte
    assert "lancer_sonde_complet_1rep &" in texte
    assert 'wait "$pid_sonde"' in texte and 'wait "$pid_etalon"' in texte

    # Masquage des 3 familles de secrets
    for marqueur in ("[MASQUE_GH]", "[MASQUE_HCLOUD]", "[MASQUE_VAST]"):
        assert marqueur in texte


# ---------------------------------------------------------------------------
# 2. VÉRIFICATION DE programme_monde_plante_v4.fusionner() SUR LARGEURS MIXTES
# ---------------------------------------------------------------------------


def _preparer_depot_code_v2_temporaire(tmp_root: Path):
    """Extrait un clone temporaire propre de `0ce9e35110d93dd916e85b1191a2613b101e772d` depuis le `.git` local
    (lecture seule, aucun fichier du dépôt principal modifié, R12)."""
    repo_tmp = tmp_root / "repo_code_v2"
    git_bin = shutil.which("git")

    # Voie 1 : clone local sans réseau depuis REPO_PRINCIPAL au commit exact 0ce9e35110...
    if git_bin and (REPO_PRINCIPAL / ".git").exists():
        repo_tmp.mkdir(parents=True, exist_ok=True)
        r_ar = subprocess.run(
            [git_bin, "-C", str(REPO_PRINCIPAL), "archive", COMMIT_CODE_OFFICIEL, "src"],
            capture_output=True,
        )
        if r_ar.returncode == 0:
            with tarfile.open(fileobj=io.BytesIO(r_ar.stdout), mode="r:") as tf:
                tf.extractall(repo_tmp)
            subprocess.run([git_bin, "init", "-q", str(repo_tmp)], check=True)
            subprocess.run([git_bin, "-C", str(repo_tmp), "config", "user.name", "t"], check=True)
            subprocess.run([git_bin, "-C", str(repo_tmp), "config", "user.email", "t@t"], check=True)
            subprocess.run([git_bin, "-C", str(repo_tmp), "add", "-A"], check=True)
            r_co = subprocess.run([git_bin, "-C", str(repo_tmp), "-c", "commit.gpgsign=false", "commit", "-q", "-m", "c"], capture_output=True)
            if r_co.returncode == 0 and (repo_tmp / "src/controle_ia/sondes_v2/programme_monde_plante_v4.py").is_file():
                for mod_name in [k for k in list(sys.modules) if k == "controle_ia" or k.startswith("controle_ia.")]:
                    sys.modules.pop(mod_name, None)
                sys.path.insert(0, str(repo_tmp / "src"))
                from controle_ia.gardes import GardeArret
                from controle_ia.scellement import verifier
                from controle_ia.sondes_v2 import programme_monde_plante_v4 as p
                return p, GardeArret, verifier, True, repo_tmp

    # Voie 2 : si l'arbre courant ou CODE_V2_EXTRAIT possède déjà tout sondes_v2
    try:
        src_principal = Path(r"C:\Users\lciri\.gemini\antigravity-cli\brain\cd7c89b9-9752-4dac-b846-2c58efd89737\scratch\wt-b8-puissance") / "src" / "controle_ia"
        if src_principal.is_dir() and CODE_V2_EXTRAIT.is_dir() and (CODE_V2_EXTRAIT / "statistiques_v2.py").is_file():
            pkg_ci = repo_tmp / "src" / "controle_ia"
            pkg_sv2 = pkg_ci / "sondes_v2"
            pkg_sv2.mkdir(parents=True, exist_ok=True)
            for f in src_principal.iterdir():
                if f.is_file() and f.suffix == ".py":
                    shutil.copy2(f, pkg_ci / f.name)
            for f in CODE_V2_EXTRAIT.iterdir():
                if f.is_file() and f.suffix in (".py", ".json", ".sha256"):
                    shutil.copy2(f, pkg_sv2 / f.name)
            if git_bin:
                subprocess.run([git_bin, "init", str(repo_tmp)], check=True, capture_output=True)
                subprocess.run([git_bin, "-C", str(repo_tmp), "config", "user.name", "t"], check=True, capture_output=True)
                subprocess.run([git_bin, "-C", str(repo_tmp), "config", "user.email", "t@t"], check=True, capture_output=True)
                subprocess.run([git_bin, "-C", str(repo_tmp), "add", "-A"], check=True, capture_output=True)
                subprocess.run([git_bin, "-C", str(repo_tmp), "-c", "commit.gpgsign=false", "commit", "-m", "init"], check=True, capture_output=True)
            for mod_name in [k for k in list(sys.modules) if k == "controle_ia" or k.startswith("controle_ia.")]:
                sys.modules.pop(mod_name, None)
            sys.path.insert(0, str(repo_tmp / "src"))
            from controle_ia.gardes import GardeArret
            from controle_ia.scellement import verifier
            from controle_ia.sondes_v2 import programme_monde_plante_v4 as p
            return p, GardeArret, verifier, True, repo_tmp
    except PermissionError:
        pass
    return None


def test_fusionner_largeurs_mixtes_10_5_et_10_6_4_identique_octet() -> None:
    try:
        import numpy  # noqa: F401
        import scipy  # noqa: F401
        import sklearn  # noqa: F401
    except ImportError:
        try:
            import pytest
            pytest.skip("numpy/scipy/scikit-learn non installés dans cet interpréteur Python")
        except ImportError:
            print("INFO : saut du test dynamique numpy/scipy/sklearn (interpréteur sans dépendances scientifiques)")
            return

    with tempfile.TemporaryDirectory(prefix="sondes_v2_fusion_v3_", ignore_cleanup_errors=True) as td:
        tmp_path = Path(td)
        prep = _preparer_depot_code_v2_temporaire(tmp_path)
        if prep is None:
            try:
                import pytest
                pytest.skip(f"Commit {COMMIT_CODE_OFFICIEL} non présent dans le clone local de {REPO_PRINCIPAL}")
            except ImportError:
                print(f"INFO : saut de l'exécution de programme_monde_plante_v4 ({COMMIT_CODE_OFFICIEL} absent du .git local)")
                return

        p, GardeArret, verifier, depot_git_propre, _ = prep
        assert depot_git_propre

        seuils = {"alpha": 0.05, "u_fort": 0.9}
        cas_mini = [(4, 2, 8, 2)]
        mondes_mini = ["identite_seule", "trace_forte", "intensite_4"]
        note_meta = {"chemin": "/opt/entree/note-des-effectifs-sondes-v2-v1.md", "sha256": SHA_NOTE_OFFICIEL}

        # --- Cas 1 (exigence explicite § 3) : repliques=25 découpé en [0,10), [10,20), [20,25) ---
        dir_25_unique = tmp_path / "r25_unique"
        ch_unique_25 = p.executer(
            dir_25_unique, "etalon", cas_mini, repliques=25, n_nul=19, n_tirages=80,
            seuils=seuils, d=16, entropie=int(ENTROPIE_OFFICIELLE), mondes=mondes_mini,
            n_nul_identite=20, note_effectifs=note_meta,
        )
        rap_unique_25 = json.loads(ch_unique_25.read_text(encoding="utf-8"))

        dir_25_mixte = tmp_path / "r25_mixte"
        chemins_25 = [
            p.executer(
                dir_25_mixte, "etalon", cas_mini, repliques=25, n_nul=19, n_tirages=80,
                seuils=seuils, d=16, entropie=int(ENTROPIE_OFFICIELLE), mondes=mondes_mini,
                n_nul_identite=20, plage=pl, note_effectifs=note_meta,
            )
            for pl in [(0, 10), (10, 20), (20, 25)]
        ]
        syn_fusion_25 = p.fusionner(chemins_25)
        assert p._canon(syn_fusion_25) == p._canon(rap_unique_25["synthese"]), (
            "La fusion [0,10)+[10,20)+[20,25) diffère à l'octet d'un processus unique [0,25)"
        )
        cible_syn_25 = p.ecrire_synthese_fusionnee(
            chemins_25, dir_25_mixte / f"synthese-fusionnee-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}.json"
        )
        verifier(cible_syn_25)
        corps_syn_25 = json.loads(cible_syn_25.read_text(encoding="utf-8"))
        assert len(corps_syn_25["rapports"]) == 3
        assert p._canon(corps_syn_25["synthese"]) == p._canon(rap_unique_25["synthese"])

        # --- Cas 2 (exigence 64 cœurs PAS_ETALON=6 + queue de 4 répliques) :
        #     repliques=26 découpé en [0,10) (10) + [10,16) (6) + [16,22) (6) + [22,26) (4, analogue de [496,500)) ---
        dir_26_unique = tmp_path / "r26_unique"
        ch_unique_26 = p.executer(
            dir_26_unique, "etalon", cas_mini, repliques=26, n_nul=19, n_tirages=80,
            seuils=seuils, d=16, entropie=int(ENTROPIE_OFFICIELLE), mondes=mondes_mini,
            n_nul_identite=20, note_effectifs=note_meta,
        )
        rap_unique_26 = json.loads(ch_unique_26.read_text(encoding="utf-8"))

        dir_26_mixte = tmp_path / "r26_mixte"
        plages_26 = [(0, 10)] + decouper_plages_comme_amorce(10, 26, 6)
        assert plages_26 == [(0, 10), (10, 16), (16, 22), (22, 26)]
        chemins_26 = [
            p.executer(
                dir_26_mixte, "etalon", cas_mini, repliques=26, n_nul=19, n_tirages=80,
                seuils=seuils, d=16, entropie=int(ENTROPIE_OFFICIELLE), mondes=mondes_mini,
                n_nul_identite=20, plage=pl, note_effectifs=note_meta,
            )
            for pl in plages_26
        ]
        cible_syn_26 = p.ecrire_synthese_fusionnee(
            chemins_26, dir_26_mixte / f"synthese-fusionnee-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}.json"
        )
        verifier(cible_syn_26)
        corps_syn_26 = json.loads(cible_syn_26.read_text(encoding="utf-8"))
        assert p._canon(corps_syn_26["synthese"]) == p._canon(rap_unique_26["synthese"]), (
            "La fusion [0,10)+[10,16)+[16,22)+[22,26) (PAS_ETALON=6 + queue de 4) diffère d'un processus unique"
        )

        # --- Gardes négatives de fusionner() ---
        try:
            p.fusionner(chemins_25[:2])
            raise AssertionError("fusionner aurait dû rejeter une couverture incomplète [0, 20) / 25")
        except GardeArret as exc:
            assert "couvrent [0, 20) au lieu de [0, 25)" in str(exc)

        try:
            p.fusionner([chemins_25[0], chemins_25[2]])
            raise AssertionError("fusionner aurait dû rejeter des plages non contiguës")
        except GardeArret as exc:
            assert "non contiguës" in str(exc)

        dir_25_bad = tmp_path / "r25_bad_note"
        ch_bad = p.executer(
            dir_25_bad, "etalon", cas_mini, repliques=25, n_nul=19, n_tirages=80,
            seuils=seuils, d=16, entropie=int(ENTROPIE_OFFICIELLE), mondes=mondes_mini,
            n_nul_identite=20, plage=(20, 25),
            note_effectifs={"chemin": "/workspace/entree/note-des-effectifs-sondes-v2-v1.md", "sha256": SHA_NOTE_OFFICIEL},
        )
        try:
            p.fusionner([chemins_25[0], chemins_25[1], ch_bad])
            raise AssertionError("fusionner aurait dû rejeter un chemin note_effectifs discordant")
        except GardeArret as exc:
            assert "arguments" in str(exc)


def test_verification_13_rapports_amont_extraits_localement() -> None:
    """Vérifie l'intégrité SHA-256 et les métadonnées des 13 tranches réelles `[0, 130)` si accessibles."""
    try:
        if not BRUT_ETALON_AMONT.is_dir():
            return
    except PermissionError:
        return
    attendus = [(de, de + 10) for de in range(0, 130, 10)]
    for de, a in attendus:
        nom = f"rapport-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}-r{de}-{a}.json"
        f_json = BRUT_ETALON_AMONT / nom
        f_sha = BRUT_ETALON_AMONT / f"{nom}.sha256"
        assert f_json.is_file() and f_sha.is_file(), f"Tranche amont manquante : {nom}"
        ligne_sha = f_sha.read_text(encoding="utf-8").strip()
        assert ligne_sha == f"{sha256_file(f_json)}  {nom}", f"SHA-256 invalide pour {nom}"
        meta = json.loads(f_json.read_text(encoding="utf-8"))
        assert meta["plage"] == [de, a]
        assert meta["mode"] == "etalon"
        assert meta["verites_sha256"] == SHA_VERITES_OFFICIEL
        assert meta["graines"]["entropie_racine"] == ENTROPIE_OFFICIELLE
        assert meta["manifeste"]["commit"] == COMMIT_CODE_OFFICIEL
        assert meta["manifeste"]["depot_propre"] is True
        assert meta["arguments"]["note_effectifs"] == {
            "chemin": "/opt/entree/note-des-effectifs-sondes-v2-v1.md",
            "sha256": SHA_NOTE_OFFICIEL,
        }


# ---------------------------------------------------------------------------
# 3. ESSAIS DYNAMIQUES BOUT-EN-BOUT SOUS BASH (VAST.AI 64 CŒURS & HETZNER)
# ---------------------------------------------------------------------------


def _trouver_bash_fonctionnel() -> str | None:
    candidats: list[str] = []
    if sys.platform == "win32":
        for p in (
            r"C:\Program Files\Git\bin\bash.exe",
            r"C:\Program Files\Git\usr\bin\bash.exe",
        ):
            if Path(p).is_file():
                candidats.append(p)
    b_which = shutil.which("bash")
    if b_which and b_which not in candidats:
        if not (sys.platform == "win32" and b_which.lower().endswith(r"\system32\bash.exe")):
            candidats.append(b_which)

    for b in candidats:
        try:
            r = subprocess.run(
                [b, "-c", "command -v git curl sha256sum tar split sed awk grep tr"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            if r.returncode == 0:
                return b
        except Exception:
            continue
    return None


def _vers_chemin_bash(bash_bin: str, p: Path) -> str:
    s = str(p.resolve())
    if sys.platform == "win32" and len(s) >= 3 and s[1:3] == ":\\":
        drive = s[0].lower()
        rest = s[3:].replace("\\", "/")
        return f"/{drive}/{rest}"
    return s


class FakeCloudServer:
    """Serveur HTTP local simulant à la fois l'API Hetzner (/v1/servers/<ID> + metadata)
    et l'API Vast.ai (/api/v0/instances/<ID>/)."""

    def __init__(self, expected_hc_token: str, hetzner_id: str, expected_vast_key: str) -> None:
        self.expected_hc_token = expected_hc_token
        self.hetzner_id = hetzner_id
        self.expected_vast_key = expected_vast_key
        self.hetzner_deleted: list[str] = []
        self.vast_deleted: list[str] = []
        self.auth_errors: list[str] = []
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, fmt, *args):  # noqa: A002
                return

            def do_GET(self):
                if self.path == "/hetzner/v1/metadata/instance-id":
                    body = outer.hetzner_id.encode("utf-8")
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    self.send_response(404)
                    self.end_headers()

            def do_DELETE(self):
                auth = self.headers.get("Authorization", "")
                if self.path.startswith("/v1/servers/"):
                    if auth != f"Bearer {outer.expected_hc_token}":
                        outer.auth_errors.append(f"hetzner:{auth}")
                        self.send_response(401)
                        self.end_headers()
                        return
                    outer.hetzner_deleted.append(self.path[len("/v1/servers/"):])
                    body = b'{"action":{"status":"success"}}'
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                elif self.path.startswith("/api/v0/instances/") and self.path.endswith("/"):
                    if auth != f"Bearer {outer.expected_vast_key}":
                        outer.auth_errors.append(f"vast:{auth}")
                        self.send_response(401)
                        self.end_headers()
                        return
                    vid = self.path[len("/api/v0/instances/"):-1]
                    outer.vast_deleted.append(vid)
                    body = b'{"success":true}'
                    self.send_response(200)
                    self.send_header("Content-Length", str(len(body)))
                    self.end_headers()
                    self.wfile.write(body)
                else:
                    self.send_response(404)
                    self.end_headers()

        self.httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.port = self.httpd.server_address[1]
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()

    def close(self) -> None:
        self.httpd.shutdown()
        self.httpd.server_close()


def _creer_depot_bare_avec_amont_etalon(root: Path, chemin_note_attendu: str) -> tuple[Path, str, str, str, str]:
    bare = root / "origin.git"
    seed = root / "seed"
    subprocess.run(["git", "init", "--bare", str(bare)], check=True, capture_output=True)
    subprocess.run(["git", "init", str(seed)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "config", "user.name", "test-r5-v3"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "config", "user.email", "test@r5.local"], check=True, capture_output=True)

    # 1. main
    subprocess.run(["git", "-C", str(seed), "checkout", "-B", "main"], check=True, capture_output=True)
    note_dir = seed / "docs/notes/sondes-v2-effectifs-et-correspondance-v1"
    note_dir.mkdir(parents=True, exist_ok=True)
    note_p = note_dir / "note-des-effectifs-sondes-v2-v1.md"
    note_p.write_bytes(b"# Note effectifs factice R5 v3\n")
    sha_note = sha256_file(note_p)
    (note_dir / "note-des-effectifs-sondes-v2-v1.md.sha256").write_bytes(
        f"{sha_note}  note-des-effectifs-sondes-v2-v1.md\n".encode("utf-8")
    )
    subprocess.run(["git", "-C", str(seed), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "commit", "-m", "main"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "push", str(bare), "main:refs/heads/main"], check=True, capture_output=True)

    # 2. sondes-v2/code-v2
    subprocess.run(["git", "-C", str(seed), "checkout", "--orphan", "code_tmp"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "rm", "-rf", "."], check=True, capture_output=True)
    v_dir = seed / "src/controle_ia/sondes_v2"
    v_dir.mkdir(parents=True, exist_ok=True)
    verites_p = v_dir / "verites_mondes_plantes_v4.json"
    verites_p.write_bytes(b'{"format":"verites-v4-test-v3"}\n')
    sha_verites = sha256_file(verites_p)
    subprocess.run(["git", "-C", str(seed), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "commit", "-m", "code-v2"], check=True, capture_output=True)
    commit_code = subprocess.run(
        ["git", "-C", str(seed), "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    subprocess.run(
        ["git", "-C", str(seed), "push", str(bare), "HEAD:refs/heads/sondes-v2/code-v2"],
        check=True,
        capture_output=True,
    )

    # 3. calcul/sondes-v2-epreuve-plantee-v4 : 13 rapports r0-10 .. r120-130 + .sha256
    subprocess.run(["git", "-C", str(seed), "checkout", "--orphan", "amont_tmp"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "rm", "-rf", "."], check=True, capture_output=True)
    et_dir = seed / "epreuve-plantee-v4" / "etalon"
    et_dir.mkdir(parents=True, exist_ok=True)
    for de in range(0, 130, 10):
        a = de + 10
        nom = f"rapport-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}-r{de}-{a}.json"
        corps = (
            json.dumps(
                {
                    "format": "rapport-monde-plante-v4",
                    "mode": "etalon",
                    "plage": [de, a],
                    "verites_sha256": sha_verites,
                    "graines": {"entropie_racine": ENTROPIE_OFFICIELLE},
                    "arguments": {
                        "note_effectifs": {"chemin": chemin_note_attendu, "sha256": sha_note},
                    },
                    "manifeste": {"commit": commit_code, "depot_propre": True, "reserves": []},
                },
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
        (et_dir / nom).write_bytes(corps)
        (et_dir / f"{nom}.sha256").write_bytes(f"{sha256_bytes(corps)}  {nom}\n".encode("utf-8"))
    subprocess.run(["git", "-C", str(seed), "add", "-A"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(seed), "commit", "-m", "amont 13 tranches"], check=True, capture_output=True)
    commit_amont = subprocess.run(
        ["git", "-C", str(seed), "rev-parse", "HEAD"], check=True, capture_output=True, text=True
    ).stdout.strip()
    subprocess.run(
        ["git", "-C", str(seed), "push", str(bare), "HEAD:refs/heads/calcul/sondes-v2-epreuve-plantee-v4"],
        check=True,
        capture_output=True,
    )
    _rmtree_win(seed)
    return bare, commit_code, sha_verites, sha_note, commit_amont


def _ecrire_faux_runner(script_sh: Path, py_exe_bash: str, comportement_complet: str) -> None:
    py_helper = script_sh.with_suffix(".py")
    code_py = f"""import base64, glob, hashlib, json, os, sys, time
from pathlib import Path

mode = sys.argv[1]
outdir = Path(sys.argv[2])
entropie = sys.argv[3]
de_g = int(sys.argv[4])
a_g = int(sys.argv[5])
pas = int(sys.argv[6])
workers = int(sys.argv[7]) if len(sys.argv) > 7 else 0
outdir.mkdir(parents=True, exist_ok=True)

# Vérifier qu'AUCUNE variable d'environnement secrète n'est exposée au processus fils Python !
INTERDITES = ("GH_TOKEN_ENV", "VAST_API_KEY_ENV", "HCLOUD_TOKEN_ENV", "GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY", "HCLOUD_TOKEN", "GH_TOK")
presentes = [k for k in INTERDITES if k in os.environ]
if presentes:
    raise SystemExit(f"FUITE ENVIRONNEMENT FILS PYTHON : {{presentes}}")

def sceller_test(p: Path, raw: bytes) -> None:
    p.write_bytes(raw)
    h = hashlib.sha256(raw).hexdigest()
    p.with_name(p.name + ".sha256").write_bytes(f"{{h}}  {{p.name}}\\n".encode("utf-8"))

# Émettre volontairement les 3 faux secrets sur stderr pour éprouver filtrer_secrets_log
print("FUITE_TEST_GH: https://x-access-token:{FAKE_GH_TOKEN}@github.com/lciric/controle-ia-travail.git", file=sys.stderr, flush=True)
print("FUITE_TEST_HC: {FAKE_HCLOUD_TOKEN}", file=sys.stderr, flush=True)
print("FUITE_TEST_VAST: Authorization: Bearer {FAKE_VAST_KEY}", file=sys.stderr, flush=True)

if mode == "sonde_complet_1rep":
    t_debut = time.time()
    time.sleep(0.35)
    t_fin = time.time()
    sceller_test(
        outdir / f"rapport-monde-plante-v4-complet-{{entropie}}.json",
        (json.dumps({{"mode": "complet", "repliques": 1, "duree_secondes": round(t_fin - t_debut, 4), "t_debut": t_debut, "t_fin": t_fin}}) + "\\n").encode("utf-8"),
    )
    sys.exit(0)

if mode == "etalon":
    assert de_g == 130 and a_g == 500, (de_g, a_g)
    existants = sorted(glob.glob(str(outdir / f"rapport-monde-plante-v4-etalon-{{entropie}}-r*.json")))
    assert len(existants) == 13, f"13 rapports amont attendus avant calcul suite, trouvé {{len(existants)}}"
    t_debut = time.time()
    time.sleep(0.35)
    t_fin = time.time()
    for d in range(de_g, a_g, pas):
        a = min(a_g, d + pas)
        sceller_test(
            outdir / f"rapport-monde-plante-v4-etalon-{{entropie}}-r{{d}}-{{a}}.json",
            (json.dumps({{"mode": "etalon", "plage": [d, a], "workers": workers, "t_debut": t_debut, "t_fin": t_fin}}) + "\\n").encode("utf-8"),
        )
    tous = sorted(glob.glob(str(outdir / f"rapport-monde-plante-v4-etalon-{{entropie}}-r*.json")))
    sceller_test(
        outdir / f"synthese-fusionnee-monde-plante-v4-etalon-{{entropie}}.json",
        (json.dumps({{"mode": "etalon", "nb_rapports_fusionnes": len(tous), "workers_etalon": workers, "t_debut": t_debut, "t_fin": t_fin}}) + "\\n").encode("utf-8"),
    )
    sys.exit(0)

if mode == "complet":
    if {comportement_complet!r} == "sleep":
        time.sleep(60)
        sys.exit(0)
    sceller_test(
        outdir / f"rapport-monde-plante-v4-complet-{{entropie}}-r{{de_g}}-{{a_g}}.json",
        (json.dumps({{"mode": "complet", "plage": [de_g, a_g]}}) + "\\n").encode("utf-8"),
    )
    if de_g == 0 and a_g == 500:
        sceller_test(
            outdir / f"synthese-fusionnee-monde-plante-v4-complet-{{entropie}}.json",
            (json.dumps({{"mode": "complet", "synthese": True}}) + "\\n").encode("utf-8"),
        )
    rng = os.urandom(90000) if {comportement_complet!r} == "large" else b"petit"
    b64 = base64.b64encode(rng).decode("ascii")
    sceller_test(outdir / "journal-gels-monde-plante-v4-complet-r0-5.jsonl", (json.dumps({{"b": b64}}) + "\\n").encode("utf-8"))
"""
    py_helper.write_bytes(code_py.encode("utf-8"))
    py_helper_b = _vers_chemin_bash("", py_helper)
    sh_body = f"#!/usr/bin/env bash\nexec \"{py_exe_bash}\" -B \"{py_helper_b}\" \"$@\"\n"
    script_sh.write_bytes(sh_body.encode("utf-8"))
    script_sh.chmod(0o700)


def test_execution_bout_en_bout_bash_r5_v3() -> None:
    bash_bin = _trouver_bash_fonctionnel()
    if bash_bin is None:
        try:
            import pytest
            pytest.skip("bash + outils GNU (git/curl/sha256sum/tar) non disponibles sur cet hôte")
        except ImportError:
            print("INFO : saut des essais dynamiques bash (bash non disponible)")
            return

    amorce_b = _vers_chemin_bash(bash_bin, SCRIPT_AMORCE)
    py_b = _vers_chemin_bash(bash_bin, Path(sys.executable))

    # 3.0 Vérification syntaxique bash -n
    r_syn = subprocess.run([bash_bin, "-n", amorce_b], capture_output=True, text=True)
    assert r_syn.returncode == 0, f"bash -n a échoué : {r_syn.stderr}"

    with tempfile.TemporaryDirectory(prefix="test_amorce_v3_r5_", ignore_cleanup_errors=True) as td:
        root = Path(td)
        srv = FakeCloudServer(FAKE_HCLOUD_TOKEN, FAKE_HETZNER_ID, FAKE_VAST_KEY)
        try:
            run_vast = root / "run_vast"
            # Sous MSYS2/Git Bash sur Windows, les arguments `/c/...` passés à python.exe natif sont
            # convertis en `C:/...` par le runtime MSYS2 : utiliser `Path(run_vast / "entree").resolve().as_posix()`
            # si python est win32, sinon le chemin bash direct.
            if sys.platform == "win32":
                chemin_note_vast_dans_python = str((run_vast / "entree" / "note-des-effectifs-sondes-v2-v1.md").resolve()).replace("\\", "/")
            else:
                chemin_note_vast_dans_python = f"{_vers_chemin_bash(bash_bin, run_vast / 'entree')}/note-des-effectifs-sondes-v2-v1.md"

            bare, commit_code, sha_verites, sha_note, commit_amont = _creer_depot_bare_avec_amont_etalon(
                root, chemin_note_vast_dans_python
            )
            bare_b = _vers_chemin_bash(bash_bin, bare)
            runner_vast = root / "runner_vast.sh"
            _ecrire_faux_runner(runner_vast, py_b, "large")
            runner_vast_b = _vers_chemin_bash(bash_bin, runner_vast)

            def env_commun(run_dir: Path) -> dict[str, str]:
                env = os.environ.copy()
                for k in ("GH_TOKEN_ENV", "VAST_API_KEY_ENV", "HCLOUD_TOKEN_ENV", "GITHUB_TOKEN", "GH_TOKEN", "VAST_API_KEY", "HCLOUD_TOKEN", "CONTAINER_ID", "VAST_INSTANCE_ID"):
                    env.pop(k, None)
                env.update({
                    "COMMIT_CODE": commit_code,
                    "ENTROPIE": ENTROPIE_OFFICIELLE,
                    "SHA_VERITES": sha_verites,
                    "SHA_NOTE": sha_note,
                    "COMMIT_AMONT_ETALON": commit_amont,
                    "REPO_URL": bare_b,
                    "HCLOUD_API": f"http://127.0.0.1:{srv.port}/v1",
                    "METADATA_URL": f"http://127.0.0.1:{srv.port}/hetzner/v1/metadata/instance-id",
                    "VAST_API_URL": f"http://127.0.0.1:{srv.port}/api/v0",
                    "GH_TOKEN_FILE": _vers_chemin_bash(bash_bin, run_dir / ".gh_token"),
                    "HCLOUD_TOKEN_FILE": _vers_chemin_bash(bash_bin, run_dir / ".hcloud_token"),
                    "VAST_API_KEY_FILE": _vers_chemin_bash(bash_bin, run_dir / ".vast_api_key"),
                    "WORK": _vers_chemin_bash(bash_bin, run_dir / "work"),
                    "ENTREE": _vers_chemin_bash(bash_bin, run_dir / "entree"),
                    "SORTIE": _vers_chemin_bash(bash_bin, run_dir / "sortie"),
                    "LOG": _vers_chemin_bash(bash_bin, run_dir / "epreuve.log"),
                    "SKIP_ENV_INSTALL": "1",
                    "PY_BIN": py_b,
                    "SIMULER_MODE_CMD": runner_vast_b,
                    "N_WORKERS": "4",
                })
                return env

            # --- 3.1 Gardes de rejet immédiat (rc != 0, zéro DELETE émis) ---
            e1 = env_commun(root / "g_mono")
            e1["N_WORKERS"] = "1"
            e1["EXIGER_MULTICOEUR"] = "1"
            r1 = subprocess.run([bash_bin, amorce_b], env=e1, capture_output=True, text=True)
            assert r1.returncode == 1 and "MULTICŒUR" in r1.stderr

            e2 = env_commun(root / "g_url")
            e2["REPO_URL"] = f"https://x-access-token:{FAKE_GH_TOKEN}@github.com/lciric/controle-ia-travail.git"
            r2 = subprocess.run([bash_bin, amorce_b], env=e2, capture_output=True, text=True)
            assert r2.returncode == 1 and "ARRÊT SÉCURITÉ" in r2.stderr

            for br_interdite in ("main", "calcul/sondes-v2-epreuve-plantee-v4"):
                eb = env_commun(root / f"g_br_{br_interdite.replace('/', '_')}")
                eb["BRANCHE_SORTIE"] = br_interdite
                rb = subprocess.run([bash_bin, amorce_b], env=eb, capture_output=True, text=True)
                assert rb.returncode == 1 and "R12" in rb.stderr, (br_interdite, rb.returncode, rb.stderr)

            for vid_noir in VAST_BLACKLIST:
                ev1 = env_commun(root / f"g_vast_id_{vid_noir}")
                ev1["FOURNISSEUR"] = "vast"
                ev1["VAST_API_KEY_ENV"] = FAKE_VAST_KEY
                ev1["VAST_INSTANCE_ID"] = vid_noir
                rv1 = subprocess.run([bash_bin, amorce_b], env=ev1, capture_output=True, text=True)
                assert rv1.returncode == 1 and "liste noire" in rv1.stderr

                ev2 = env_commun(root / f"g_vast_cid_{vid_noir}")
                ev2["FOURNISSEUR"] = "vast"
                ev2["VAST_API_KEY_ENV"] = FAKE_VAST_KEY
                ev2["CONTAINER_ID"] = vid_noir
                rv2 = subprocess.run([bash_bin, amorce_b], env=ev2, capture_output=True, text=True)
                assert rv2.returncode == 1 and "liste noire" in rv2.stderr

            for vid_invalide in ("abc123", "058936096", "../123"):
                evi = env_commun(root / "g_vast_bad")
                evi["FOURNISSEUR"] = "vast"
                evi["VAST_INSTANCE_ID"] = vid_invalide
                rvi = subprocess.run([bash_bin, amorce_b], env=evi, capture_output=True, text=True)
                assert rvi.returncode == 1
            assert srv.vast_deleted == [] and srv.hetzner_deleted == []

            # --- 3.2 Scénario Vast.ai 64 cœurs : MODE_RUN=etalon_suite_et_sonde_complet_1rep ---
            ev_ok = env_commun(run_vast)
            ev_ok.update({
                "MODE_RUN": "etalon_suite_et_sonde_complet_1rep",
                "N_WORKERS": "64",
                "PAS_ETALON": "6",
                "FOURNISSEUR": "auto",
                "GH_TOKEN_ENV": FAKE_GH_TOKEN, "HCLOUD_TOKEN_ENV": FAKE_HCLOUD_TOKEN,
                "VAST_API_KEY_ENV": FAKE_VAST_KEY,
                "CONTAINER_ID": FAKE_VAST_ID,
                "WATCHDOG_SECONDES": "120",
            })
            rv_ok = subprocess.run([bash_bin, amorce_b], env=ev_ok, capture_output=True, text=True)
            assert rv_ok.returncode == 0, f"Échec scénario Vast 64 cœurs:\nSTDOUT:\n{rv_ok.stdout}\nSTDERR:\n{rv_ok.stderr}"
            assert "Mode parallèle activé (N_WORKERS=64 >= 63)" in rv_ok.stdout
            assert "RAPATRIEMENT PROUVÉ : calcul/sondes-v2-epreuve-plantee-v4-suite @" in rv_ok.stdout
            assert srv.vast_deleted == [FAKE_VAST_ID], f"DELETE Vast non reçu: {srv.vast_deleted}"
            assert srv.hetzner_deleted == []
            assert not srv.auth_errors, srv.auth_errors

            amont_head = subprocess.run(
                ["git", "ls-remote", str(bare), "refs/heads/calcul/sondes-v2-epreuve-plantee-v4"],
                check=True, capture_output=True, text=True,
            ).stdout.split()[0]
            assert amont_head == commit_amont

            verif_vast = root / "verif_vast"
            subprocess.run(
                ["git", "-c", "core.autocrlf=false", "clone", "--branch", "calcul/sondes-v2-epreuve-plantee-v4-suite", str(bare), str(verif_vast)],
                check=True, capture_output=True,
            )
            ep_v = verif_vast / "epreuve-plantee-v4"
            rapports_et = sorted((ep_v / "etalon").glob("rapport-monde-plante-v4-etalon-*-r*.json"))
            assert len(rapports_et) == 75, f"75 rapports étalon attendus (13 amont + 62 suite), trouvé {len(rapports_et)}"
            assert (ep_v / "etalon" / f"rapport-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}-r496-500.json").is_file()
            syn_et = json.loads(
                (ep_v / "etalon" / f"synthese-fusionnee-monde-plante-v4-etalon-{ENTROPIE_OFFICIELLE}.json").read_text(encoding="utf-8")
            )
            assert syn_et["nb_rapports_fusionnes"] == 75
            assert syn_et["workers_etalon"] == 63

            meta_sonde_p = ep_v / "sonde-complet-1rep-meta.json"
            assert meta_sonde_p.is_file() and (ep_v / "sonde-complet-1rep-meta.json.sha256").is_file()
            assert not (ep_v / "complet").exists(), "$SORTIE/complet ne doit pas être pollué par sonde_complet_1rep"
            meta_sonde = json.loads(meta_sonde_p.read_text(encoding="utf-8"))
            assert meta_sonde["repliques_sondees"] == 1 and meta_sonde["duree_secondes"] >= 0.3

            for sf in sorted(ep_v.rglob("*.sha256")):
                ligne = sf.read_text(encoding="utf-8").strip()
                sha_att, nom_cible = ligne.split("  ", 1)
                assert sha256_file(sf.parent / nom_cible) == sha_att
            for f in ep_v.rglob("*"):
                if f.is_file():
                    raw = f.read_bytes()
                    assert FAKE_GH_TOKEN.encode() not in raw
                    assert FAKE_HCLOUD_TOKEN.encode() not in raw
                    assert FAKE_VAST_KEY.encode() not in raw
            log_v = (ep_v / "journal-execution.log").read_text(encoding="utf-8")
            assert "[MASQUE_GH]" in log_v and "[MASQUE_HCLOUD]" in log_v and "[MASQUE_VAST]" in log_v

            # --- 3.3 Scénario Hetzner R10 timeout (`WATCHDOG_SECONDES=3`) ---
            srv.hetzner_deleted.clear()
            srv.vast_deleted.clear()
            run_hc = root / "run_hc"
            if sys.platform == "win32":
                chemin_note_hc_dans_python = str((run_hc / "entree" / "note-des-effectifs-sondes-v2-v1.md").resolve()).replace("\\", "/")
            else:
                chemin_note_hc_dans_python = f"{_vers_chemin_bash(bash_bin, run_hc / 'entree')}/note-des-effectifs-sondes-v2-v1.md"
            bare_hc, cc_hc, sv_hc, sn_hc, ca_hc = _creer_depot_bare_avec_amont_etalon(
                root / "hc_repo", chemin_note_hc_dans_python
            )
            runner_sleep = root / "runner_sleep.sh"
            _ecrire_faux_runner(runner_sleep, py_b, "sleep")
            eh = env_commun(run_hc)
            eh.update({
                "MODE_RUN": "etalon_suite_et_complet",
                "REPO_URL": _vers_chemin_bash(bash_bin, bare_hc),
                "COMMIT_CODE": cc_hc,
                "SHA_VERITES": sv_hc,
                "SHA_NOTE": sn_hc,
                "COMMIT_AMONT_ETALON": ca_hc,
                "FOURNISSEUR": "hetzner",
                "HCLOUD_TOKEN_ENV": FAKE_HCLOUD_TOKEN,
                "GH_TOKEN_ENV": FAKE_GH_TOKEN,
                "SIMULER_MODE_CMD": _vers_chemin_bash(bash_bin, runner_sleep),
                "WATCHDOG_SECONDES": "3",
                "BRANCHE_SORTIE": "calcul/sondes-v2-epreuve-plantee-v4-suite-hc",
            })
            rh = subprocess.run([bash_bin, amorce_b], env=eh, capture_output=True, text=True)
            assert rh.returncode == 124, f"rc=124 attendu sur timeout R10, reçu {rh.returncode}\nSTDOUT:\n{rh.stdout}\nSTDERR:\n{rh.stderr}"
            assert srv.hetzner_deleted == [FAKE_HETZNER_ID]
        finally:
            srv.close()


def main() -> int:
    fonctions = [
        test_amorce_v3_lf_strict_et_encodage_utf8,
        test_amorce_v3_ordre_nproc_avant_omp_et_garde_multicoeur,
        test_amorce_v3_xargs_sans_n1_avec_replace_et_pas_etalon_6,
        test_amorce_v3_gardes_securite_branches_vast_et_63e_coeur,
        test_verification_13_rapports_amont_extraits_localement,
        test_fusionner_largeurs_mixtes_10_5_et_10_6_4_identique_octet,
        test_execution_bout_en_bout_bash_r5_v3,
    ]
    for fn in fonctions:
        fn()
        print(f"OK : {fn.__name__}")
    for p_f in (SCRIPT_AMORCE, Path(__file__).resolve()):
        raw = p_f.read_bytes()
        print(f"SHA256 {p_f.name} ({len(raw)} octets, CR={b'\\r' in raw}) = {sha256_bytes(raw)}")
    print(f"SUCCÈS COMPLET ({len(fonctions)}/{len(fonctions)} suites de tests vérifiées)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
